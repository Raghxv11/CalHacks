import json
import os
from threading import Lock

RESOURCE_FILE = 'shared_resources.json'
file_lock = Lock()

def init_resource_file():
    with file_lock:
        if not os.path.exists(RESOURCE_FILE):
            with open(RESOURCE_FILE, 'w') as f:
                json.dump({}, f)

def add_resources(agent_address, resources):
    init_resource_file()  # Ensure file exists
    with file_lock:
        with open(RESOURCE_FILE, 'r+') as f:
            data = json.load(f)
            data[agent_address] = resources
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

def get_all_resources():
    init_resource_file()  # Ensure file exists
    with file_lock:
        with open(RESOURCE_FILE, 'r') as f:
            return json.load(f)