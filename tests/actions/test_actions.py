import pytest
from actions.actions import add, sub, power


@pytest.mark.parametrize(
    "nums, ans",
    (
        ((1, 2), 3),
        ((5, 3), 8),
    ),
)
def test_add(nums, ans):
    assert add(*nums) == ans


@pytest.mark.parametrize(
    "nums, ans",
    (
        ((2, 1), 1),
        ((5, 3), 2),
    ),
)
def test_sub(nums, ans):
    assert sub(*nums) == ans


@pytest.mark.parametrize('a, b, ans', [(2, 2, 4), (3, 2, 9), (2, 3, 8)])
def test_power(a, b, ans):
    assert power(a, b) == ans
