import sys
from collections import deque
from typing import List

sys.tracebacklimit = 0


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if the start or end cell is blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        directions = [
            [0, 1],
            [1, 1],
            [-1, 1],
            [1, -1],
            [-1, -1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]
        rows = cols = len(grid)
        seen = set()

        queue = deque()  # (row, column, distance)
        queue.append((0, 0, 1))
        # Perform BFS
        while queue:
            curr_row, curr_col, distance = queue.popleft()

            # Check if we reached the end cell
            if curr_row == rows - 1 and curr_col == cols - 1:
                return distance

            for dx, dy in directions:
                new_row = curr_row + dx
                new_col = curr_col + dy

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and (new_row, new_col) not in seen
                    and grid[new_row][new_col] == 0
                ):
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, distance + 1))

        return -1


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("shortestPathBinaryMatrix", 2, grid=[[0, 1], [1, 0]])
run_test(
    "shortestPathBinaryMatrix",
    4,
    grid=[
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ],
)
run_test(
    "shortestPathBinaryMatrix",
    -1,
    grid=[
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ],
)
