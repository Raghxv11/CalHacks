from uagents import Agent, Context, Model, Bureau
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

def create_contributor_agent(name, port, seed, gpu_count, memory_gb, availability_hours):
    agent = Agent(
        name=name,
        port=port,
        seed=seed,
        endpoint=[f"http://127.0.0.1:{port}/submit"],
    )

    fund_agent_if_low(agent.wallet.address())

    @agent.on_message(model=ResourceRequest)
    async def handle_resource_request(ctx: Context, sender: str, request: ResourceRequest):
        ctx.logger.info(f"Received resource request from {sender}: {request.json()}")
        
        if gpu_count >= request.required_gpu and memory_gb >= request.required_memory:
            offer = ResourceOffer(
                agent_address=agent.address,
                gpu_count=gpu_count,
                memory_gb=memory_gb,
                availability_hours=availability_hours
            )
            ctx.logger.info(f"Sending resource offer to {sender}")
            await ctx.send(sender, offer)
        else:
            ctx.logger.info("Cannot fulfill the resource request")

    return agent

# Create multiple contributor agents
contributor_agents = [
    create_contributor_agent("Contributor1", 8001, "Seed1", 2, 16, 8),
    create_contributor_agent("Contributor2", 8002, "Seed2", 4, 32, 12),
    create_contributor_agent("Contributor3", 8003, "Seed3", 1, 8, 24),
    create_contributor_agent("Contributor4", 8004, "Seed4", 8, 64, 6),
    create_contributor_agent("Contributor5", 8005, "Seed5", 2, 16, 10),
]

if __name__ == "__main__":
    bureau = Bureau()
    for agent in contributor_agents:
        bureau.add(agent)
        print(f"Contributor Agent Address: {agent.address}")
    
    # Run all agents concurrently using the Bureau
    bureau.run()