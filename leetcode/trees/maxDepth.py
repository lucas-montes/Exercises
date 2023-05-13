import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "maxDepth")
run_test(RESULT, [ARGS], "maxDepth")
# run_test(RESULT, [ARGS], 'maxDepth')
