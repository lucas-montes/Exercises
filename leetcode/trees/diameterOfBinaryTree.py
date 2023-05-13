import sys
from collections import deque
from typing import List

sys.tracebacklimit = 0


class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "diameterOfBinaryTree")
run_test(RESULT, [ARGS], "diameterOfBinaryTree")
# run_test(RESULT, [ARGS], 'diameterOfBinaryTree')
