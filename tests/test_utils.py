import pytest

from aoc24.utils import get_modules, get_solutions


def test_get_modules():
    assert get_modules(pytest, "fixture") == [pytest.fixture]


def test_get_solutions():
    assert get_solutions("data/tests/", test=True) == {"data/tests/day1a.txt": (11, 31)}
