import sys

from typing import List

sys.tracebacklimit = 0

# Use monotonic decreasing stack


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            # As it's a stack is FILO first in last out.
            while stack and temp > temperatures[stack[-1]]:
                day = (
                    stack.pop()
                )  # the first value of the stack, so the last value added
                result[day] = index - day
            stack.append(index)

        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(
    [1, 1, 4, 2, 1, 1, 0, 0], [[73, 74, 75, 71, 69, 72, 76, 73]], "dailyTemperatures"
)
run_test([1, 1, 1, 0], [[30, 40, 50, 60]], "dailyTemperatures")
run_test([1, 1, 0], [[30, 60, 90]], "dailyTemperatures")
