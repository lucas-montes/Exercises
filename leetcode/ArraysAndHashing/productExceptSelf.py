from typing import List
from functools import reduce
import operator


class Solution:
    def prod(self, iterable):
        return reduce(operator.mul, iterable, 1)

    def calculate(self, nums, index):
        new_l = nums.copy()
        new_l.pop(index)
        return self.prod(new_l)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        seen = {}
        for index, num in enumerate(nums):
            if num in seen:
                prod = seen[num]
            else:
                prod = self.calculate(nums, index)
                seen[num] = prod
            result.append(prod)

        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test([24, 12, 8, 6], [[1, 2, 3, 4]], "productExceptSelf")
run_test([0, 0, 9, 0, 0], [[-1, 1, 0, -3, 3]], "productExceptSelf")
