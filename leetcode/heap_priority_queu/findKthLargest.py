import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "findKthLargest")
run_test(RESULT, [ARGS], "findKthLargest")
# run_test(RESULT, [ARGS], 'findKthLargest')
