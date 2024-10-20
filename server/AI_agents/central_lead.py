from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

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

# This list should be populated with the addresses of the contributor agents
CONTRIBUTOR_ADDRESSES = [
    "agent1qfz3995z8u5meuyrx4j7c8s8pjalwxr4r3wzhqmegctpxrm7fzq0796tnyw",
    "agent1qvuqy30ty7xs7tuqncl7rh2wmr3pt63m9mn4gehzgrvkjhj6pemu7u2zzsx",
    "agent1q2aqsmjsa9gz5v3szmq9ulkh9rndcrenc9c8spev350fxknfx49kypptklj",
    "agent1qwyc7aawedjqyj70x6qur3gjcq30att024drelsy3fgl336t5dn2gehct8y",
    "agent1q0cfgxwgn27p9qunk7ttsnj5w3zw4nlylatkjrr0ty07e0a5m9s57w7l7yj",
]

ProjectLeadAgent = Agent(
    name="ProjectLeadAgent",
    port=8007,
    seed="ProjectLeadSeed",
    endpoint=["http://127.0.0.1:8007/submit"],
)

fund_agent_if_low(ProjectLeadAgent.wallet.address())

@ProjectLeadAgent.on_interval(period=10.0)
async def request_resources(ctx: Context):
    request = ResourceRequest(
        project_name="AI Model Training",
        required_gpu=2,
        required_memory=16,
        task_description="Training a large language model"
    )
    for address in CONTRIBUTOR_ADDRESSES:
        ctx.logger.info(f"Requesting resources from {address}")
        await ctx.send(address, request)

@ProjectLeadAgent.on_message(model=ResourceOffer)
async def handle_resource_offer(ctx: Context, sender: str, offer: ResourceOffer):
    ctx.logger.info(f"Received resource offer from {sender}: {offer.json()}")
    # Here you can implement logic to accept or reject the offer

if __name__ == "__main__":
    ProjectLeadAgent.run()