import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def reverse(self, x: int) -> int:
        f = int(str(abs(x))[::-1])
        if x < 0:
            f *= -1
        return f if f.bit_length() < 32 else 0


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(321, [123], "reverse")
run_test(-321, [-123], "reverse")
run_test(21, [120], "reverse")
