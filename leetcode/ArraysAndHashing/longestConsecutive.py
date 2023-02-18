from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums = sorted(list(set(nums)))
        max_followed = 1
        len_nums = len(nums)
        if len_nums == 1:
            return 1
        half_nums = len_nums // 2
        index = 0
        while index < len_nums:
            current_num = nums[index]
            following = 1
            for sub_index in range(1, len_nums):
                second_index = index + sub_index

                if (
                    second_index < len_nums
                    and nums[second_index] == current_num + sub_index
                ):
                    following += 1
                elif max_followed > half_nums:
                    return max_followed
                else:
                    break
                max_followed = max(following, max_followed)
            index = second_index
        return max_followed


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test(4, [[100, 4, 200, 1, 3, 2]], "longestConsecutive")
run_test(9, [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "longestConsecutive")
run_test(3, [[1, 2, 0, 1]], "longestConsecutive")
run_test(
    5,
    [[4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]],
    "longestConsecutive",
)
run_test(1, [[0]], "longestConsecutive")
run_test(1, [[-6, -1, -1, 9, -8, -6, -6, 4, 4, -3, -8, -1]], "longestConsecutive")
run_test(0, [[]], "longestConsecutive")
