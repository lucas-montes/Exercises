import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def trap(self, height: List[int]) -> int:
        len_h = len(height)
        left, right = 0, len_h - 1
        result = 0
        if len_h > 1:
            max_l, max_r = height[left], height[right]
            while left < right:
                if max_l < max_r:
                    left += 1
                    current = height[left]
                    max_l = max(max_l, current)
                    max_to_add = max_l
                else:
                    right -= 1
                    current = height[right]
                    max_r = max(max_r, current)
                    max_to_add = max_r
                result += max_to_add - current
        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(6, [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], "trap")
run_test(9, [[4, 2, 0, 3, 2, 5]], "trap")
run_test(0, [[0]], "trap")
run_test(1, [[4, 2, 3]], "trap")
