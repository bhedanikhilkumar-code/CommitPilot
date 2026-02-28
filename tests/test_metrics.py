from src.metrics import completion_percent, remaining_commits


def test_completion_percent():
    state = {"goal_commits": 100, "completed_commits": 25}
    assert completion_percent(state) == 25.0


def test_remaining_commits():
    state = {"goal_commits": 100, "completed_commits": 67}
    assert remaining_commits(state) == 33
