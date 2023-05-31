import math
import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def euclidean(self, x, y):
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: math.pow(x[0], 2) + math.pow(x[1], 2))[:k]


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test([[-2, 2]], [[[1, 3], [-2, 2]], 1], "kClosest")
run_test([[3, 3], [-2, 4]], [[[3, 3], [5, -1], [-2, 4]], 2], "kClosest")
# run_test(RESULT, [ARGS], 'kClosest')
