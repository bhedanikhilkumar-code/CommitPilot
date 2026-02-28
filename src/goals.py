from src.state import load_state, save_state

def set_goal(value: int):
    state = load_state()
    state['goal_commits'] = max(1, int(value))
    save_state(state)
