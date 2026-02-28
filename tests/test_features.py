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

def test_validate_goal_30():
    assert validate_goal_30(100)
    assert not validate_goal_30(0)

def test_validate_goal_38():
    assert validate_goal_38(100)
    assert not validate_goal_38(0)

def test_validate_goal_46():
    assert validate_goal_46(100)
    assert not validate_goal_46(0)

def test_validate_goal_54():
    assert validate_goal_54(100)
    assert not validate_goal_54(0)

def test_validate_goal_62():
    assert validate_goal_62(100)
    assert not validate_goal_62(0)

def test_validate_goal_70():
    assert validate_goal_70(100)
    assert not validate_goal_70(0)
