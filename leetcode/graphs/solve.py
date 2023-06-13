import sys
from collections import deque
from typing import List

sys.tracebacklimit = 0


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = range(len(board)), range(len(board[0]))
        seen = set()
        is_x = set()
        is_o = set()

        def dfs(r, c):
            q = deque()
            seen.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                around = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                sr = 0
                for dr, dc in around:
                    r, c = row + dr, col + dc
                    if r in rows and c in cols:
                        if (r, c) not in seen:
                            if board[r][c] == "X":
                                sr += 1
                                is_x.add((r, c))
                            else:
                                is_o.add((r, c))
                                q.append((r, c))
                            seen.add((r, c))
                        else:
                            if (r, c) in is_x:
                                sr += 1
                if sr == 4:
                    board[r][c] = "X"

        for r in rows:
            for c in cols:
                if board[r][c] == "O" and (r, c) not in seen:
                    is_o.add((r, c))
                    dfs(r, c)
                else:
                    seen.add((r, c))
                    is_x.add((r, c))
        return board


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(
    "solve",
    [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ],
    board=[
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ],
)
run_test("solve", [["X"]], [["X"]])
