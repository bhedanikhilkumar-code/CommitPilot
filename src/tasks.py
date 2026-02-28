from src.state import load_state, save_state

def add_task(title: str):
    state = load_state()
    state.setdefault('tasks', []).append({'title': title, 'done': False})
    save_state(state)

def list_tasks():
    state = load_state()
    return state.get('tasks', [])
