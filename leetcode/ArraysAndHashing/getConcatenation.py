import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("getConcatenation", [1, 2, 1, 1, 2, 1], nums=[1, 2, 1])
run_test("getConcatenation", [1, 3, 2, 1, 1, 3, 2, 1], nums=[1, 3, 2, 1])
