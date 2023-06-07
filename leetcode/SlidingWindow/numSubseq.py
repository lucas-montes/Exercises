import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        result = 0
        l, r = 0, 1
        seen = {}
        while True:
            f = nums[l]
            u = nums[r]
            if u in seen:
            if (f+u) <= target:
                result += 1
        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(4, [[3, 5, 6, 7], 9], "numSubseq")
run_test(6, [[3, 3, 6, 8], 10], "numSubseq")
run_test(61, [[2, 3, 3, 4, 6, 7], 12], "numSubseq")
