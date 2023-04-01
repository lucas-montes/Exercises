import sys
import math
from typing import List

sys.tracebacklimit = 0


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_res = r
        while l <= r:
            m = l + (r - l) // 2
            # List comprehension is 20% faster than loop
            result = sum(math.ceil(pile / m) for pile in piles)
            if result <= h:
                # Using an if else is 1% faster
                min_res = min(min_res, m)
                r = m - 1
            else:
                l = m + 1

        return min_res


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(4, [[3, 6, 7, 11], 8], "minEatingSpeed")
run_test(30, [[30, 11, 23, 4, 20], 5], "minEatingSpeed")
run_test(23, [[30, 11, 23, 4, 20], 6], "minEatingSpeed")
