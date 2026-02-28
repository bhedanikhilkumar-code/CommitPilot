from src.state import load_state
from src.metrics import completion_percent

def main():
    state = load_state()
    pct = completion_percent(state)
    print(f"CommitPilot: {state['completed_commits']}/{state['goal_commits']} ({pct}%)")
