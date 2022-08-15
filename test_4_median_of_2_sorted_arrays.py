from typing import List

import pytest


def find_median(nums1: List[int], nums2: List[int]) -> float:
    """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
    """
    a = min(nums1, nums2, key=len)
    b = max(nums2, nums1, key=len)

    total = len(a) + len(b)
    half = total // 2

    l, r = 0, len(a) - 1
    while True:
        mid_a = (r + l) // 2
        mid_b = half - mid_a - 2

        a_l = a[mid_a] if mid_a >= 0 else float("-infinity")
        a_r = a[mid_a + 1] if mid_a + 1 < len(a) else float("infinity")
        b_l = b[mid_b] if mid_b >= 0 else float("-infinity")
        b_r = b[mid_b + 1] if mid_b + 1 < len(b) else float("infinity")

        if a_l <= b_r and b_l <= a_r:
            if total % 2:
                return min(a_r, b_r)
            else:
                return (max(a_l, b_l) + min(a_r, b_r)) / 2
        elif a_l > b_r:
            r = mid_a - 1
        elif b_l > a_r:
            l = mid_a + 1


@pytest.mark.parametrize("nums1,nums2,output", (([1, 3], [2], 2.0),
                                                ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], 4.0),
                                                ([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], 3.5),
                                                ([1, 2], [3, 4], 2.5),
                                                ([1, 4], [2, 3], 2.5),
                                                ([1, 3], [2, 7], 2.5),
                                                ([2], [1, 3, 4], 2.5),
                                                ([1], [2, 3, 4], 2.5)))
def test_1(nums1, nums2, output):
    assert find_median(nums1, nums2) == output
