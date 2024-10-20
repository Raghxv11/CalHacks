from uagents import Agent, Context, Model
from shared_resources import add_resources, get_all_resources

class ResourceRequest(Model):
    project_name: str
    required_gpu: int
    required_memory: int
    task_description: str

class ResourceOffer(Model):
    agent_address: str
    gpu_count: int
    memory_gb: int
    availability_hours: int

ContributorAgent = Agent(
    name="ContributorAgent",
    port=8003,
    seed="iandandnfonvoisnovn",
    endpoint=["http://127.0.0.1:8003/submit"],
)

print(f"Contributor Agent Address: {ContributorAgent.address}")

# Simulated available resources
AVAILABLE_RESOURCES = {
    "gpu_count": 8,
    "memory_gb": 8,
    "availability_hours": 4
}

@ContributorAgent.on_interval(period=5.0)
async def update_resources(ctx: Context):
    add_resources(ContributorAgent.address, AVAILABLE_RESOURCES)
    ctx.logger.info(f"Updated resources in shared file: {AVAILABLE_RESOURCES}")
    
    # Check if lead agent is already registered
    all_resources = get_all_resources()
    lead_agent = next((addr for addr, res in all_resources.items() if res.get("role") == "lead"), None)
    if lead_agent:
        ctx.logger.info(f"Lead agent found: {lead_agent}")
    else:
        ctx.logger.info("Lead agent not found. Will wait for resource requests.")

@ContributorAgent.on_message(model=ResourceRequest)
async def handle_resource_request(ctx: Context, sender: str, request: ResourceRequest):
    ctx.logger.info(f"Received resource request from {sender}: {request.json()}")
    
    offer = ResourceOffer(
        agent_address=ContributorAgent.address,
        **AVAILABLE_RESOURCES
    )
    ctx.logger.info(f"Sending resource offer to {sender}")
    await ctx.send(sender, offer)

if __name__ == "__main__":
    ContributorAgent.run()