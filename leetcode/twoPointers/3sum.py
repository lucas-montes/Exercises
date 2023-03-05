from typing import List


class Solution:
    def twoSum(
        self,
        result: List,
        current_index: int,
        current_number: int,
        numbers: List[int],
    ) -> List[int]:
        l, r = current_index + 1, len(numbers) - 1
        while l < r:
            cumulative_sum = current_number + numbers[l] + numbers[r]

            if cumulative_sum > 0:  # some is greater, we need to decrease
                r -= 1
            elif cumulative_sum < 0:  # some is to small, we make it bigger
                l += 1
            else:
                result.append([current_number, numbers[l], numbers[r]])  # equal to zero
                l += 1
                while (
                    numbers[l] == numbers[l - 1] and l < r
                ):  # if we have already seen the left value we move on
                    l += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # O(nlogn) for sorting
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue  # if current num is same as past one, skip
            self.twoSum(result, index, num, nums)  # O(n^2) nested loop

        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test([[-1, -1, 2], [-1, 0, 1]], [[-1, 0, 1, 2, -1, -4]], "threeSum")
run_test([], [[0, 1, 1]], "threeSum")
run_test([[0, 0, 0]], [[0, 0, 0]], "threeSum")
run_test([], [[1, 2, -2, -1]], "threeSum")
