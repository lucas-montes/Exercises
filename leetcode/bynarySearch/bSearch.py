import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2  # To avoid overflow error
            c = nums[m]
            if c == target:
                return m
            elif c > target:
                r = m - 1
            else:
                l = m + 1
        return -1


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(4, [[-1, 0, 3, 5, 9, 12], 9], "search")
run_test(-1, [[-1, 0, 3, 5, 9, 12], 2], "search")
run_test(0, [[5], 5], "search")
run_test(0, [[-1, 0, 3, 5, 9, 12], -1], "search")
