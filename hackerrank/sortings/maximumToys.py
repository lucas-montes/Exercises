import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def maximumToys(self, prices, k):
        l, r = 0, 1
        m_t = 0
        prices.sort()
        while True:
            sub_p = prices[l:r]
            if sum(sub_p) <= k:
                if len(sub_p) > m_t:
                    m_t = len(sub_p)
                r += 1
            else:
                break
        return m_t


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("maximumToys", 4, prices=[1, 12, 5, 111, 200, 1000, 10], k=50)
