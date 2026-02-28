from src.state import load_state, save_state


def plan_slots_3(slots: int = 4):
    state = load_state()
    tasks = state.get('tasks', [])
    plan = []
    for i, task in enumerate(tasks[:slots]):
        plan.append({'slot': i+1, 'task': task.get('title', 'Untitled')})
    return plan
