def completion_percent(state):
    goal = max(1, state['goal_commits'])
    return round((state['completed_commits'] / goal) * 100, 2)


def remaining_commits(state):
    return max(0, state['goal_commits'] - state['completed_commits'])


# checkpoint_102: retained for history cleanliness
