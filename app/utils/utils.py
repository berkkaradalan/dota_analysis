import time
import uuid

def generate_id():
    return str(uuid.uuid4())

def get_current_time():
    return time.time()