from src.state import load_state, save_state

def set_goal(value: int):
    state = load_state()
    state['goal_commits'] = max(1, int(value))
    save_state(state)

def increment_completed(count: int = 1):
    state = load_state()
    state['completed_commits'] = state.get('completed_commits', 0) + int(count)
    save_state(state)
