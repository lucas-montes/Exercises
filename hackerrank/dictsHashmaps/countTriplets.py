import sys
from itertools import combinations
from typing import List

sys.tracebacklimit = 0


class Solution:
    """
    r: common ratio. Is the value used to multiply each value in the arr to get the following
    value in the geometric progression.
    Ex: arr = [1, 2, 4] r= 2 'cause 1 * 2 = 2; 2 * 2 = 4

    create a sliding window taking n values until n+1 > arr[i] * r**2
    Fail for some eadge cases
    """

    def count_combinations(self, arr: List, left: int, right: int) -> List:
        # we check that the values that belong to the indeces
        # aren't repeated
        return [
            comb
            for comb in combinations(range(left, right), 3)
            if len({arr[i] for i in comb}) == 3
        ]

    def countTriplets(self, arr: List, r: int):
        left = 0
        right = 3
        result = []
        while right < len(arr):
            if arr[right] == arr[left] * r**2:
                # here we have all the possible values to join
                result.extend(
                    self.count_combinations(
                        arr,
                        left,
                        right + 1,
                    )
                )
                left += 1
            else:
                right += 1
        return len(set(result))


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"Test with expected value {expected} succeed ✅")


run_test(2, [[1, 2, 2, 4], 2], "countTriplets")
run_test(6, [[1, 3, 9, 9, 27, 81], 3], "countTriplets")
run_test(4, [[1, 5, 5, 25, 125], 5], "countTriplets")
