import os
import json

def save_json(data, path):
    with open(path, "w") as f:
        f.write(json.dumps(data, indent=4))
