import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        new_sorted = []
        while left and right:
            new_sorted.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return new_sorted + left + right

    def mergeSort(self, numbers: List[int]) -> List[int]:
        len_numbers = len(numbers)
        if len_numbers == 1:
            return numbers
        half = len_numbers // 2
        return self.merge(
            self.mergeSort(numbers[:half]), self.mergeSort(numbers[half:])
        )


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test([0, 5], [[5], [0]], "merge")
run_test([0, 5, 6], [[5, 6], [0]], "merge")
run_test([0, 4, 5], [[5], [0, 4]], "merge")

run_test([5], [[5]], "mergeSort")
run_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [[5, 1, 2, 4, 8, 0, 6, 9, 7, 3]], "mergeSort")
