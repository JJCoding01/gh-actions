import pytest
from actions.actions import add


@pytest.mark.parametrize(
    "nums, ans",
    (
        ((1, 2), 3),
        ((5, 3), 8),
    ),
)
def test_add(nums, ans):
    assert add(*nums) == ans
