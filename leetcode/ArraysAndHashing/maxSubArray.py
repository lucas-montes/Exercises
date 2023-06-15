import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, current = float("-inf"), 0
        for num in nums:
            current += num

            result = max(result, current)
            current = max(current, 0)
        return result


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("maxSubArray", 6, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
run_test("maxSubArray", 1, nums=[1])
run_test("maxSubArray", 23, nums=[5, 4, -1, 7, 8])
