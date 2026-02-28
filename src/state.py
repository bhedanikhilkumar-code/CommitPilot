import json
from pathlib import Path

STATE_PATH = Path('data/state.json')

def load_state():
    return json.loads(STATE_PATH.read_text(encoding='utf-8'))
