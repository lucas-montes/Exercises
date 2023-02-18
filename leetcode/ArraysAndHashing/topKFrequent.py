from typing import List


class Solution:
    def get_most_seen(self, max_s, k):
        most_seen = sorted(max_s.keys(), reverse=True)
        result = []
        for seen in most_seen:
            for all_seen in max_s[seen]:
                if k > 0:
                    result.append(all_seen)
                    k -= 1
                else:
                    break
        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        max_s = {}

        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1

        for key, value in seen.items():
            if value in max_s:
                max_s[value].append(key)
            else:
                max_s[value] = [key]

        return self.get_most_seen(max_s, k)


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test([1, 2], [[1, 1, 1, 2, 2, 3], 2], "topKFrequent")
run_test([1], [[1], 1], "topKFrequent")
run_test([-1, 2], [[4, 1, -1, 2, -1, 2, 3], 2], "topKFrequent")
run_test([1, 2], [[1, 2, 2, 2, 2, 2, 2, 22, 1, 1, 1, 1, 1, 5], 2], "topKFrequent")

# runtime 100 ms beats 89.95%
# memory 18.7 MB beats 67.34%
