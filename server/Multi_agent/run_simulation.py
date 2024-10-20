from uagents import Bureau
from lead_agent import ProjectLeadAgent
from contributor_agent import create_contributor_agent
from dynamic_moderator import DynamicModeratorAgent

NUM_CONTRIBUTORS = 5  # Change this to the desired number of contributors

if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8000/submit"], port=8000)
    
    # Add lead agent
    bureau.add(ProjectLeadAgent)
    
    # Add contributor agents
    for i in range(NUM_CONTRIBUTORS):
        contributor = create_contributor_agent(8001 + i)
        bureau.add(contributor)
    
    # Add dynamic moderator agent
    bureau.add(DynamicModeratorAgent)
    
    bureau.run()