import sys
from collections import deque
from typing import List

sys.tracebacklimit = 0


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        l = r = 0
        maxis: List[int] = []
        save = deque()
        # monotonically decreasing queue

        # retreiving numbers is O(1), so saving the indexes will allow us to
        # know when to remove left
        while r < len(nums):
            r_num = nums[r]
            while save and nums[save[-1]] < r_num:
                # We pop the smallest values from our deque, the one at the right
                save.pop()
            save.append(r)

            # we remove the left index as isn't in our window anymore
            if l > save[0]:
                save.popleft()

            if r + 1 >= k:
                maxis.append(nums[save[0]])
                l += 1
            r += 1
        return maxis


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test([3, 3, 5, 5, 6, 7], [[1, 3, -1, -3, 5, 3, 6, 7], 3], "maxSlidingWindow")
run_test([1], [[1], 1], "maxSlidingWindow")
run_test([7, 4], [[7, 2, 4], 2], "maxSlidingWindow")
