from src.state import load_state


def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_2(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_10(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_18(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_26(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_34(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_42(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_50(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_58(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_66(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_74(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_82(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_90(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_98(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_106(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_114(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_122(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_130(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_138(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_146(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_154(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_162(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_170(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_178(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_186(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_194(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}

def snapshot_metrics():
    state = load_state()
    goal = max(1, state.get('goal_commits', 1))
    done = state.get('completed_commits', 0)
    return {'goal': goal, 'done': done, 'pct': round((done/goal)*100, 2)}


def velocity_hint_202(days: int = 7):
    metrics = snapshot_metrics()
    remaining = max(0, metrics['goal'] - metrics['done'])
    return {'days': days, 'remaining': remaining, 'daily_needed': round(remaining/max(1, days), 2)}
