import sys
from typing import List

sys.tracebacklimit = 0

https: // leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2  # To avoid overflow error
            middle_num = nums[m]
            if middle_num == target:
                return m
            elif middle_num < target:
                l = m + 1
            else:
                pass


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(2, [[1, 3, 5, 6], 5], 'searchInsert')
run_test(1, [[1, 3, 5, 6], 2], 'searchInsert')
run_test(4, [[1, 3, 5, 6], 7], 'searchInsert')
