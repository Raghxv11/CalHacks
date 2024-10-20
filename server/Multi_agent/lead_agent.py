# from uagents import Agent, Context, Model
# from shared_resources import init_resource_file, get_all_resources, add_resources

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

# ProjectLeadAgent = Agent(
#     name="ProjectLeadAgent",
#     port=8000,
#     seed="ProjectLeadSeed",
#     endpoint=["http://127.0.0.1:8000/submit"],
# )

# print(f"Project Lead Agent Address: {ProjectLeadAgent.address}")

# @ProjectLeadAgent.on_interval(period=1.0)
# async def initialize_lead_agent(ctx: Context):
#     init_resource_file()
#     all_resources = get_all_resources()
#     if ProjectLeadAgent.address not in all_resources:
#         lead_info = {
#             "role": "lead",
#             "requirements": {
#                 "project_name": "AI Model Training",
#                 "required_gpu": 30,
#                 "required_memory": 64,
#                 "task_description": "Training a large language model"
#             }
#         }
#         add_resources(ProjectLeadAgent.address, lead_info)
#         ctx.logger.info("Added lead agent to shared resource file")

#     ctx.logger.info(f"Current available resources from shared file: {all_resources}")

# @ProjectLeadAgent.on_message(model=ResourceOffer)
# async def handle_resource_offer(ctx: Context, sender: str, offer: ResourceOffer):
#     ctx.logger.info(f"Received resource offer from {sender}: {offer.json()}")

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

ProjectLeadAgent = Agent(
    name="ProjectLeadAgent",
    port=8000,
    seed="ProjectLeadSeed",
    endpoint=["http://127.0.0.1:8000/submit"],
)

print(f"Project Lead Agent Address: {ProjectLeadAgent.address}")

resources_requested = False

@ProjectLeadAgent.on_interval(period=5.0)
async def initialize_and_request_resources(ctx: Context):
    global resources_requested
    if not resources_requested:
        init_resource_file()
        all_resources = get_all_resources()
        if ProjectLeadAgent.address not in all_resources:
            lead_info = {
                "role": "lead",
                "requirements": {
                    "project_name": "AI Model Training",
                    "required_gpu": 30,
                    "required_memory": 64,
                    "task_description": "Training a large language model"
                }
            }
            add_resources(ProjectLeadAgent.address, lead_info)
            ctx.logger.info("Added lead agent to shared resource file")

        ctx.logger.info(f"Current available resources from shared file: {all_resources}")

        request = ResourceRequest(**lead_info["requirements"])
        for address in all_resources.keys():
            if address != ProjectLeadAgent.address:
                ctx.logger.info(f"Requesting resources from: {address}")
                await ctx.send(address, request)
        
        resources_requested = True
    else:
        ctx.logger.info("Resources have already been requested.")

@ProjectLeadAgent.on_message(model=ResourceOffer)
async def handle_resource_offer(ctx: Context, sender: str, offer: ResourceOffer):
    ctx.logger.info(f"Received resource offer from {sender}: {offer.json()}")

if __name__ == "__main__":
    ProjectLeadAgent.run()