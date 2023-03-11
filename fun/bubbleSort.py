import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def bubbleSort(self, numbers: List[int]) -> List[int]:
        ordered = False
        len_nums = len(numbers)
        while not ordered:
            ordered = True
            for index, value in enumerate(numbers):
                if index < len_nums - 1:
                    next_value = numbers[index + 1]
                    if next_value < value:
                        numbers[index] = next_value
                        numbers[index + 1] = value
                        ordered = False
        return numbers


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [[5, 1, 2, 4, 8, 0, 6, 9, 7, 3]], "bubbleSort")
