import json
from pathlib import Path

STATE_PATH = Path('data/state.json')

def load_state():
    return json.loads(STATE_PATH.read_text(encoding='utf-8'))

def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding='utf-8')
