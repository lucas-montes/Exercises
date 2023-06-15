import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def countSwaps(self, a: List[int]):
        len_a = len(a)
        swaps = 0
        swaped = True
        while swaped:
            swaped = False
            for l in range(len_a - 1):
                r = l + 1
                if a[l] > a[r]:
                    swaped = True
                    a[r], a[l] = a[l], a[r]
                    swaps += 1

        return (swaps, a[0], a[-1])


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("countSwaps", (3, 1, 6), [6, 4, 1])
