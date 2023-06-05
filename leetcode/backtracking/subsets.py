import itertools
import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) + 1):
            result.extend(list(itertools.combinations(nums, i)))
        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "subsets")
run_test(RESULT, [ARGS], "subsets")
# run_test(RESULT, [ARGS], 'subsets')
