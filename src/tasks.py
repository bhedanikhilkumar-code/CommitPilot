from src.state import load_state, save_state

def add_task(title: str):
    state = load_state()
    state.setdefault('tasks', []).append({'title': title, 'done': False})
    save_state(state)

def list_tasks():
    state = load_state()
    return state.get('tasks', [])

def complete_task(index: int):
    state = load_state()
    tasks = state.get('tasks', [])
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_state(state)
        return True
    return False
