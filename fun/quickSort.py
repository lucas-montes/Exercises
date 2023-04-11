import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def qs(self, numbers: List[int], lower: int, higher: int):
        if lower >= higher:
            return
        pivot = self.pivot(numbers, lower, higher)
        self.qs(numbers, lower, pivot - 1)
        self.qs(numbers, pivot + 1, higher)

    def pivot(self, numbers: List[int], lower: int, higher: int):
        left = lower - 1
        index = lower
        while index < higher:
            if numbers[index] <= numbers[higher]:
                left += 1
                # Swapping element at left with element at index
                (numbers[left], numbers[index]) = (numbers[index], numbers[left])
            index += 1
        # Swap the pivot(higher) element with the greater element specified by the left
        (numbers[left + 1], numbers[higher]) = (numbers[higher], numbers[left + 1])

        # Return the position from where partition is done
        return left + 1

    def quicksort(self, numbers: List[int]) -> List[int]:
        self.qs(numbers, 0, len(numbers) - 1)
        return numbers


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test([0, 1, 2, 3, 4, 5], [[3, 5, 2, 4, 1, 0]], "quicksort")
