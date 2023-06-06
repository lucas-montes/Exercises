import sys
from collections import deque
from typing import List

sys.tracebacklimit = 0


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = range(len(grid)), range(len(grid[0]))
        seen = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            seen.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r, c = row + dr, col + dc
                    if (
                        r in rows
                        and c in cols
                        and grid[r][c] == "1"
                        and (r, c) not in seen
                    ):
                        q.append((r, c))
                        seen.add((r, c))

        for r in rows:
            for c in cols:
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        return islands


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(
    1,
    [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    ],
    "numIslands",
)
run_test(
    3,
    [
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    ],
    "numIslands",
)
# run_test(RESULT, [ARGS], 'numIslands')
