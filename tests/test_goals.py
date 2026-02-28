from src.goals import set_goal
from src.state import load_state


def test_set_goal_changes_state():
    set_goal(123)
    state = load_state()
    assert state["goal_commits"] == 123
