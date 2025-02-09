import json
from pathlib import Path
import time
import uuid

def generate_id():
    return str(uuid.uuid4())

def get_current_time():
    return time.time()

def load_json(filename: str):
    DATA_DIR = Path(__file__).parent.parent / "infrastructure" / "data"
    file_path = DATA_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found in {DATA_DIR}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)