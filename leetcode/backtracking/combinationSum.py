import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        seen = {}
        result = []
        while candidates:
            c = candidates.pop(0)
            if c < target:
                i = 0
                while i < len(candidates):
                    new_c = candidates[0]
                    if new_c > target or new_c + c > target:
                        i += 1
                    else:

            elif c == target:
                result.append([c])


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("combinationSum", [[2, 2, 3], [7]], candidates=[2, 3, 6, 7], target=7)
run_test(
    "combinationSum", [[2, 2, 2, 2], [2, 3, 3], [3, 5]], candidates=[2, 3, 5], target=8
)
run_test("combinationSum", [], candidates=[2], target=1)
