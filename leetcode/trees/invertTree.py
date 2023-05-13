import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], 'invertTree')
run_test(RESULT, [ARGS], 'invertTree')
#run_test(RESULT, [ARGS], 'invertTree')

