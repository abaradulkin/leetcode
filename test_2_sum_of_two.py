import pytest


def two_sum(nums, target):
    for index, value in enumerate(nums):
        try:
            candidate = target - value
            return (index, nums[index + 1:].index(candidate) + index + 1)
        except ValueError:
            continue


@pytest.mark.parametrize("input,target,output", [([2, 7, 11, 15], 9, (0, 1)),
                                                 ([1, 2, 3, 6, 7], 5, (1, 2)),
                                                 ([3, 2, 4], 6, (1, 2))])
def test_main_func(input, target, output):
    assert two_sum(input, target) == output
