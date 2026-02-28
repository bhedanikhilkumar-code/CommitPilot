from src.state import load_state

def main():
    state = load_state()
    print(f"CommitPilot: {state['completed_commits']}/{state['goal_commits']} commits done")
