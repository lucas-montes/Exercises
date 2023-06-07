import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def isPalindrome(self, x: int) -> bool:
        f = str(x)
        return f == f[::-1]


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(True, [121], "isPalindrome")
run_test(False, [-121], "isPalindrome")
run_test(False, [10], "isPalindrome")
