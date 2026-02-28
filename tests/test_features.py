from src.features.validators import *


def test_validate_goal_6():
    assert validate_goal_6(100)
    assert not validate_goal_6(0)

def test_validate_goal_14():
    assert validate_goal_14(100)
    assert not validate_goal_14(0)

def test_validate_goal_22():
    assert validate_goal_22(100)
    assert not validate_goal_22(0)
