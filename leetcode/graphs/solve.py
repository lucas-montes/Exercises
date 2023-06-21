import sys
from collections import deque
from typing import List

sys.tracebacklimit = 0


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]
        rows, cols = len(board), len(board[0])
        seen = set()
        is_o = set()

        queue = deque()
        queue.append((0, 0))
        while queue:
            curr_row, curr_col = queue.popleft()

            for dx, dy in directions:
                new_row = curr_row + dx
                new_col = curr_col + dy
                p = (new_row, new_col)
                if 0 <= new_row < rows and 0 <= new_col < cols and p not in seen:
                    seen.add(p)
                    queue.append(p)
                    if board[new_row][new_col] == "0":
                        is_o.add(p)


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
