from src.state import load_state
from src.metrics import completion_percent

def summary_text() -> str:
    state = load_state()
    pct = completion_percent(state)
    return f"Progress: {state['completed_commits']}/{state['goal_commits']} ({pct}%)"

def task_breakdown() -> str:
    state = load_state()
    tasks = state.get('tasks', [])
    done = sum(1 for t in tasks if t.get('done'))
    total = len(tasks)
    return f"Tasks done: {done}/{total}"
