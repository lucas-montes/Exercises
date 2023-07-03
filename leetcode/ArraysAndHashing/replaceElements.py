import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        last = 0, 0
        for index, num in enumerate(arr):
            try:
                last_i, last_m = last
                if last_i <= index or last_m < num:
                    last_m = max(arr[index + 1:])
                    last = arr.index(last_m), last_m
                result.append(last_m)
            except ValueError:
                result.append(-1)
        return result


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("replaceElements", [18, 6, 6, 6, 1, -1], arr=[17, 18, 5, 4, 6, 1])
run_test("replaceElements", [-1], arr=[400])
