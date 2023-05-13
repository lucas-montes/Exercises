import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    """
    We check the height of each side. If there isn't any root then return 0 (the lowest tree).
    If the tree is unbalanced return -1.
    then verify that the tree value isn't -1
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            left, right = height(root.left), height(root.right)
            # Using any is less efficient than or
            if any([left == -1, right == -1, abs(left - right) > 1]):
                return -1
            return 1 + max(left, right)

        return height(root) != -1


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "isBalanced")
run_test(RESULT, [ARGS], "isBalanced")
# run_test(RESULT, [ARGS], 'isBalanced')


sys.tracebacklimit = 0


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(RESULT, [ARGS], "isBalanced")
run_test(RESULT, [ARGS], "isBalanced")
# run_test(RESULT, [ARGS], 'isBalanced')
