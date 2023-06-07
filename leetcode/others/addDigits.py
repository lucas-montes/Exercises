import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0  # return zero
        elif num % 9 == 0:
            return 9  # return 9 when its totally divisible by 9 such that remainder is zero
        return num % 9  # return the remainder


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(2, [38], "addDigits")
run_test(0, [0], "addDigits")
# run_test(RESULT, [ARGS], 'addDigits')
