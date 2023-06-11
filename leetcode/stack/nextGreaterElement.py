import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        seen = {}
        while nums1:
            c_n = nums1.pop(0)
            if True:
                pass
            else:
                result.append(-1)
        return result


https: // leetcode.com/problems/next-greater-element-i/


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("nextGreaterElement", [-1, 3, -1],
         nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
run_test("nextGreaterElement", [3, -1], nums1=[2, 4], nums2=[1, 2, 3, 4])
