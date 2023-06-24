import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, current, total):
            if total == target:
                result.append(current.copy())
                return
            if index >= len(candidates) or total > target:
                return

            # here we make the combinations with the next candidate
            current.append(candidates[index])
            dfs(index, current, total + candidates[index])

            # here we do not take into consideration the next candidate
            current.pop()
            dfs(index + 1, current, total)

        dfs(0, [], 0)
        return result


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("combinationSum", [[2, 2, 3], [7]], candidates=[2, 3, 6, 7], target=7)
run_test(
    "combinationSum", [[2, 2, 2, 2], [2, 3, 3], [3, 5]], candidates=[2, 3, 5], target=8
)
run_test("combinationSum", [], candidates=[2], target=1)
