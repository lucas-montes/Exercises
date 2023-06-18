import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> List[int]:
        result = []
        while nums1:
            c_n = nums1.pop(0)
            i = nums2.index(c_n)
            n = nums2[i + 1:]
            r = -1
            for m in n:
                if m > c_n:
                    r = m
                    break
            result.append(r)
        return result


# https: // leetcode.com/problems/next-greater-element-i/


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"\nResult -> {result}\nExpected -> {expected}"
    print(f"{expected} success ✅")


run_test(
    "nextGreaterElement",
    [-1, 3, -1],
    nums1=[4, 1, 2],
    nums2=[1, 3, 4, 2],
)
run_test(
    "nextGreaterElement",
    [3, -1],
    nums1=[2, 4],
    nums2=[1, 2, 3, 4],
)
run_test(
    "nextGreaterElement",
    [7, 7, 7, 7, 7],
    nums1=[1, 3, 5, 2, 4],
    nums2=[6, 5, 4, 3, 2, 1, 7],
)
