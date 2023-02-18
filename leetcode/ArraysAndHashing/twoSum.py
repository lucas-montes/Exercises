from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            dif = target - num
            if dif in seen:
                return [index, seen[dif]]
            else:
                seen[num] = index