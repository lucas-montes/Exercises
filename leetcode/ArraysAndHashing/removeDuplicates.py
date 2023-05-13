import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while True:
            try:
                if nums[i] == nums[i - 1]:
                    nums.pop(i)
                else:
                    i += 1
            except IndexError:
                break
        return len(nums)


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(2, [[1, 1, 2]], "removeDuplicates")
run_test(5, [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], "removeDuplicates")
# run_test(RESULT, [ARGS], 'removeDuplicates')
