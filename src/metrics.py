def completion_percent(state):
    goal = max(1, state['goal_commits'])
    return round((state['completed_commits'] / goal) * 100, 2)
