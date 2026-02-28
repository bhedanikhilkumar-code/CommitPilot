from src.features.validators import *


def test_validate_goal_6():
    assert validate_goal_6(100)
    assert not validate_goal_6(0)
