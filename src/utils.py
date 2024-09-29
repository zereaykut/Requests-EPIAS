from typing import List
import json

def save_json(data:dict, loc:str) -> None:
    with open(loc, "w") as f:
            f.write(json.dumps(data, indent=4))

def get_selected_powerplants():
    with open("data/selected_powerplants.json", "r", encoding="utf8") as f:
        return json.load(f).get("powerplants_info")

def get_tgt() -> str:
    """
    Get 'data/tgt.json' data
    """
    with  open("data/tgt.json", "r", encoding="utf8") as f:
        tgt = json.load(f)
    return tgt.get("tgt")
