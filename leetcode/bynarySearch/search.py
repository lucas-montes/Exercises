import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            c = nums[m]
            
            if c == target:
                return m
            if c >= nums[l]:
                #We are in the left side
                if c < target or target < nums[l]:
                    l = m +1
                else:
                    r = m - 1
            else:
                #We are in the right side
                if c > target or target > nums[r]:
                    r = m -1 
                else:
                    l = m +1

        return -1



def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(4, [[4,5,6,7,0,1,2],0], 'search')
run_test(-1, [[4,5,6,7,0,1,2],3], 'search')
run_test(-1, [[1],0], 'search')
run_test(5, [[4,5,6,7,0,1,2],1], 'search')
run_test(1, [[1,3],3], 'search')
