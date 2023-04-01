import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2  # To avoid overflow error
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <=r:
            m = l + (r - l) // 2  # To avoid overflow error
            mat = matrix[m]
            if mat[-1] >= target >= mat[0]:
                return self.search(mat, target)
            elif mat[0]<target:
                l = m + 1
            elif mat[0]>target nums[m] > target:
                r = m - 1
            else:
                

        return False


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(
    True,
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
    "searchMatrix",
)
run_test(
    False,
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
    "searchMatrix",
)
run_test(
    True,
    [[[1]], 1],
    "searchMatrix",
)
run_test(
    True,
    [[[1, 1]], 1],
    "searchMatrix",
)
