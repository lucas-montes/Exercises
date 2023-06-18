import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def get_a(self, a, b):
        xa, ya = a
        xb, yb = b
        try:
            return (yb - ya) / (xb - xa)
        except ZeroDivisionError:
            return float("inf")

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = coordinates[0]
        b = coordinates[-1]
        initial = self.get_a(a, b)
        for c in coordinates[1:-1]:
            if self.get_a(a, c) != initial:
                return False
        return True


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(
    "checkStraightLine",
    True,
    coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
)
run_test(
    "checkStraightLine",
    False,
    coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]],
)
run_test(
    "checkStraightLine",
    True,
    coordinates=[[0, 0], [0, 1], [0, -1]],
)
