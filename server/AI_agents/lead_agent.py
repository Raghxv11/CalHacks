from uagents import Agent, Context, Model
from shared_resources import init_resource_file, get_all_resources, add_resources

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

CONTRIBUTOR_ADDRESSES = [
    "agent1qfqva0rtdaqpqhgvjs52ccp93skvgpelt3sh0807fde2v3m2zkcd7rzw2q8",
    "agent1qd7c89j39lmnfz64muc3uq9y8l6jheq4au7ag5wr9ttfjerqac4vw3wffax"
    # Add more contributor addresses here
]

ProjectLeadAgent = Agent(
    name="ProjectLeadAgent",
    port=8007,
    seed="ProjectLeadSeed",
    endpoint=["http://127.0.0.1:8007/submit"],
)

print(f"Project Lead Agent Address: {ProjectLeadAgent.address}")

@ProjectLeadAgent.on_interval(period=5.0)
async def initialize_and_request_resources(ctx: Context):
    # Initialize resources (this will only create the file if it doesn't exist)
    init_resource_file()
    
    # Add lead agent's resources (if not already added)
    all_resources = get_all_resources()
    if ProjectLeadAgent.address not in all_resources:
        add_resources(ProjectLeadAgent.address, {"role": "lead"})
        ctx.logger.info("Added lead agent to shared resource file")

    ctx.logger.info(f"Current available resources from shared file: {all_resources}")

    request = ResourceRequest(
        project_name="AI Model Training",
        required_gpu=4,
        required_memory=32,
        task_description="Training a large language model"
    )

    # Request resources from known contributors
    for address in CONTRIBUTOR_ADDRESSES:
        ctx.logger.info(f"Requesting resources from known contributor: {address}")
        await ctx.send(address, request)

    # Request resources from contributors in the shared file
    for address in all_resources.keys():
        if address not in CONTRIBUTOR_ADDRESSES and address != ProjectLeadAgent.address:
            ctx.logger.info(f"Requesting resources from new contributor in shared file: {address}")
            await ctx.send(address, request)

@ProjectLeadAgent.on_message(model=ResourceOffer)
async def handle_resource_offer(ctx: Context, sender: str, offer: ResourceOffer):
    ctx.logger.info(f"Received resource offer from {sender}: {offer.json()}")
    # Here you can implement logic to accept or reject the offer
    # For example, you could update the shared file with the latest offer:
    # add_resources(sender, offer.dict())

if __name__ == "__main__":
    ProjectLeadAgent.run()