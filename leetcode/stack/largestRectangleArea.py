import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        past_heigts = []
        max_area = 0
        len_h = len(heights)
        for index, value in enumerate(heights):
            init_index = index
            while past_heigts and past_heigts[-1][1] > value:
                past_index, past_value = past_heigts.pop()
                max_area = max(max_area, (past_value * (index - past_index)))
                init_index = past_index
            past_heigts.append((init_index, value))

        for index, value in past_heigts:
            max_area = max(max_area, value * (len_h - index))
        return max_area


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(10, [[2, 1, 5, 6, 2, 3]], "largestRectangleArea")
run_test(4, [[2, 4]], "largestRectangleArea")
