import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapq.heapify(nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[self.k]
