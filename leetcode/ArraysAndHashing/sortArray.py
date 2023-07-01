import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def merge(self, right, left):
        temp = []
        while right and left:
            temp.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return temp + left + right

    def sortArray(self, nums: List[int]) -> List[int]:
        # first we split the list in two
        len_n = len(nums)
        if len_n == 1:
            return nums
        half = len_n // 2
        # we want to merge the two and split the two lists
        # until we have only one element in them
        return self.merge(self.sortArray(nums[:half]), self.sortArray(nums[half:]))


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("sortArray", [1, 2, 3, 5], nums=[5, 2, 3, 1])
run_test("sortArray", [0, 0, 1, 1, 2, 5], nums=[5, 1, 1, 2, 0, 0])
