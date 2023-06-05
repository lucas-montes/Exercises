import itertools
import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums, len(nums))


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "permute")
run_test(RESULT, [ARGS], "permute")
# run_test(RESULT, [ARGS], 'permute')
