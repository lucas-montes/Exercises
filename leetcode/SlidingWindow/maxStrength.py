import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def handle_negs(self, nums):
        if not nums:
            return 0
        if len(nums) % 2 == 0:
            x = 1
            for n in nums:
                x *= n
            return x
        else:
            if len(nums) == 1:
                return nums[0]

            t = len(nums)
            x = 1
            while t > 1:
                a = nums.pop(0)
                b = nums.pop(0)
                x *= a * b
                t = len(nums)
            return x

    def maxStrength(self, nums: List[int]) -> int:
        negs = []
        t = None
        zeros = []
        for n in nums:
            if n < 0:
                negs.append(n)
            elif n == 0:
                zeros.append(n)
            else:
                try:
                    t *= n
                except:
                    t = n
        t_n = self.handle_negs(sorted(negs))
        if t:
            if t_n > 0:
                t *= t_n
            return t
        if zeros and t_n < 0:
            return 0
        return t_n


def run_test(method, expected, *args, **kwargs):
    result = getattr(Solution(), method)(*args, **kwargs)
    assert expected == result, f"Result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test("maxStrength", 1350, nums=[3, -1, -5, 2, 5, -9])
run_test("maxStrength", 20, nums=[-4, -5, -4])
run_test("maxStrength", 0, nums=[0, -1])
run_test("maxStrength", 28, nums=[0, -4, -7])
run_test("maxStrength", 265420800, nums=[8, 6, 0, 5, -4, -8, -4, 9, -1, 6, -4, 8, -5])
