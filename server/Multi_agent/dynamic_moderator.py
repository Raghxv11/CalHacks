from uagents import Agent, Context, Model
from shared_resources import get_all_resources
import json

class ModeratorDecision(Model):
    allocated_resources: list[dict]

DynamicModeratorAgent = Agent(
    name="DynamicModeratorAgent",
    port=8010,
    seed="DynamicModeratorSeed",
    endpoint=["http://127.0.0.1:8010/submit"],
)

print(f"Dynamic Moderator Agent Address: {DynamicModeratorAgent.address}")

def allocate_resources(required_gpu, required_memory, available_resources):
    allocated = []
    total_gpu = 0
    total_memory = 0
    min_availability = float('inf')

    # Sort available resources by GPU count and memory, descending
    sorted_resources = sorted(
        [(agent, res) for agent, res in available_resources.items() if 'role' not in res],
        key=lambda x: (x[1]['gpu_count'], x[1]['memory_gb']),
        reverse=True
    )

    for agent, resources in sorted_resources:
        if total_gpu >= required_gpu and total_memory >= required_memory:
            break

        gpu = min(resources['gpu_count'], required_gpu - total_gpu)
        memory = min(resources['memory_gb'], required_memory - total_memory)
        
        if gpu > 0 or memory > 0:
            allocated.append({
                'agent_id': agent[-5:],
                'gpu_count': str(gpu),
                'memory_gb': str(memory),
                'availability_hours': str(resources['availability_hours']),
                'status': 'active'
            })
            total_gpu += gpu
            total_memory += memory
            min_availability = min(min_availability, resources['availability_hours'])

    # Add remaining inactive agents
    for agent, resources in available_resources.items():
        if agent != DynamicModeratorAgent.address and 'role' not in resources and agent[-5:] not in [a['agent_id'] for a in allocated]:
            allocated.append({
                'agent_id': agent[-5:],
                'gpu_count': str(resources['gpu_count']),
                'memory_gb': str(resources['memory_gb']),
                'availability_hours': str(resources['availability_hours']),
                'status': 'inactive'
            })

    return allocated, min_availability

@DynamicModeratorAgent.on_interval(period=10.0)
async def make_decision(ctx: Context):
    all_resources = get_all_resources()
    ctx.logger.info(f"Current available resources: {all_resources}")

    lead_agent = next((addr for addr, res in all_resources.items() if res.get("role") == "lead"), None)
    if not lead_agent:
        ctx.logger.info("Lead agent not found. Cannot make a decision.")
        return

    lead_requirements = all_resources[lead_agent].get("requirements", {})
    if not lead_requirements:
        ctx.logger.info("Lead agent requirements not found. Cannot make a decision.")
        return

    required_gpu = lead_requirements.get("required_gpu", 0)
    required_memory = lead_requirements.get("required_memory", 0)
    project_name = lead_requirements.get("project_name", "Unknown Project")

    allocated_resources, total_duration = allocate_resources(required_gpu, required_memory, all_resources)

    if allocated_resources:
        decision = ModeratorDecision(allocated_resources=allocated_resources)
        
        # Store the decision in a new JSON file
        with open('moderator_decision.json', 'w') as f:
            json.dump(allocated_resources, f, indent=2)
        
        ctx.logger.info(f"Made a decision: {json.dumps(allocated_resources, indent=2)}")
    else:
        ctx.logger.info("Couldn't allocate required resources")

if __name__ == "__main__":
    DynamicModeratorAgent.run()