from src.state import load_state
from src.metrics import completion_percent

def summary_text() -> str:
    state = load_state()
    pct = completion_percent(state)
    return f"Progress: {state['completed_commits']}/{state['goal_commits']} ({pct}%)"
