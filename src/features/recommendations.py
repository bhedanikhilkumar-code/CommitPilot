from src.state import load_state


def recommend_next_action_5():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_13():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_21():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_29():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_37():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_45():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_53():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_61():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_69():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_77():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_85():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'

def recommend_next_action_93():
    state = load_state()
    done = state.get('completed_commits', 0)
    goal = max(1, state.get('goal_commits', 1))
    if done >= goal:
        return 'Goal reached. Switch to refactor/tests.'
    if done < goal * 0.5:
        return 'Focus on small, shippable commits.'
    return 'Maintain pace with quality checks.'
