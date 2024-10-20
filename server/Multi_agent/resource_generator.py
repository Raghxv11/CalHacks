import random
import string

def generate_agent_resources():
    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]
    
    return {
        "name": random.choice(names) + '_' + ''.join(random.choices(string.ascii_lowercase, k=3)),
        "resources": {
            "gpu_count": random.randint(1, 16),
            "memory_gb": random.choice([8, 16, 32, 64, 128]),
            "availability_hours": random.randint(1, 24)
        }
    }