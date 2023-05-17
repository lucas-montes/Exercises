import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        l, r = 0, k - 1
        maxis = []
        past_big = None
        past_index = -1
        while r < len(nums):
            if past_index < l:
                past_index = -1
                past_big = None

            if not past_big or past_big < nums[r]:
                window = nums[l : r + 1]
                past_big = max(window)
                past_index = window.index(past_big)

            maxis.append(past_big)
            l += 1
            r += 1
        return maxis


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


# run_test([3, 3, 5, 5, 6, 7], [[1, 3, -1, -3, 5, 3, 6, 7], 3], "maxSlidingWindow")
# run_test([1], [[1], 1], "maxSlidingWindow")
run_test([7, 4], [[7, 2, 4], 2], "maxSlidingWindow")
