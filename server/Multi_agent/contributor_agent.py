# from uagents import Agent, Context, Model
# from shared_resources import add_resources, get_all_resources
# from resource_generator import generate_agent_resources

# class ResourceRequest(Model):
#     project_name: str
#     required_gpu: int
#     required_memory: int
#     task_description: str

# class ResourceOffer(Model):
#     agent_address: str
#     gpu_count: int
#     memory_gb: int
#     availability_hours: int

# def create_contributor_agent(port):
#     agent_data = generate_agent_resources()
    
#     ContributorAgent = Agent(
#         name=f"Contributor_{agent_data['name']}",
#         port=port,
#         seed=f"seed_{agent_data['name']}",
#         endpoint=[f"http://127.0.0.1:{port}/submit"],
#     )

#     print(f"Contributor Agent Address: {ContributorAgent.address}")

#     @ContributorAgent.on_interval(period=5.0)
#     async def update_resources(ctx: Context):
#         add_resources(ContributorAgent.address, agent_data['resources'])
#         ctx.logger.info(f"Updated resources in shared file: {agent_data['resources']}")
        
#         all_resources = get_all_resources()
#         lead_agent = next((addr for addr, res in all_resources.items() if res.get("role") == "lead"), None)
#         if lead_agent:
#             ctx.logger.info(f"Lead agent found: {lead_agent}")
#         else:
#             ctx.logger.info("Lead agent not found. Will wait for resource requests.")

#     @ContributorAgent.on_message(model=ResourceRequest)
#     async def handle_resource_request(ctx: Context, sender: str, request: ResourceRequest):
#         ctx.logger.info(f"Received resource request from {sender}: {request.json()}")
#         resources = get_all_resources()[ContributorAgent.address]
#         offer = ResourceOffer(
#             agent_address=ContributorAgent.address,
#             **resources
#         )
#         ctx.logger.info(f"Sending resource offer to {sender}")
#         await ctx.send(sender, offer)

#     return ContributorAgent

from uagents import Agent, Context, Model
from shared_resources import add_resources, get_all_resources
from resource_generator import generate_agent_resources

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

def create_contributor_agent(port):
    agent_data = generate_agent_resources()
    
    ContributorAgent = Agent(
        name=f"Contributor_{agent_data['name']}",
        port=port,
        seed=f"seed_{agent_data['name']}",
        endpoint=[f"http://127.0.0.1:{port}/submit"],
    )

    print(f"Contributor Agent Address: {ContributorAgent.address}")

    resources_updated = False

    @ContributorAgent.on_interval(period=5.0)
    async def update_resources(ctx: Context):
        nonlocal resources_updated
        if not resources_updated:
            add_resources(ContributorAgent.address, agent_data['resources'])
            ctx.logger.info(f"Updated resources in shared file: {agent_data['resources']}")
            resources_updated = True

        all_resources = get_all_resources()
        lead_agent = next((addr for addr, res in all_resources.items() if res.get("role") == "lead"), None)
        if lead_agent:
            ctx.logger.info(f"Lead agent found: {lead_agent}")
        else:
            ctx.logger.info("Lead agent not found. Will wait for resource requests.")

    @ContributorAgent.on_message(model=ResourceRequest)
    async def handle_resource_request(ctx: Context, sender: str, request: ResourceRequest):
        ctx.logger.info(f"Received resource request from {sender}: {request.json()}")
        resources = get_all_resources()[ContributorAgent.address]
        offer = ResourceOffer(
            agent_address=ContributorAgent.address,
            **resources
        )
        ctx.logger.info(f"Sending resource offer to {sender}")
        await ctx.send(sender, offer)

    return ContributorAgent