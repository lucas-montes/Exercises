import sys

from typing import List

sys.tracebacklimit = 0


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return sorted(nums)[0]


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(1, [[3,4,5,1,2]], 'findMin')
run_test(0, [[4,5,6,7,0,1,2]], 'findMin')
#run_test(RESULT, [ARGS], 'findMin')

