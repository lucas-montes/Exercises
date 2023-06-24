import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtr(index, subset):
            if index == len(nums):
                result.append(subset[::])
                return
            # all the subsets that include the current num at index
            subset.append(nums[index])
            backtr(index + 1, subset)
            subset.pop()

            # all the subsets that don't include the current num
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtr(index + 1, subset)

        backtr(0, [])
        return result


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("subsetsWithDup", [[], [1], [1, 2], [
         1, 2, 2], [2], [2, 2]], nums=[1, 2, 2])
run_test("subsetsWithDup", [[], [0]], nums=[0])
run_test(
    "subsetsWithDup", [[], [1], [1, 2], [1, 2, 3],
                       [1, 3], [2], [2, 3], [3]], [1, 2, 3]
)
