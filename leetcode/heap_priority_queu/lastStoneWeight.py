import sys
from heapq import heapify, heappop, heappush, nlargest
from typing import List

sys.tracebacklimit = 0


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            f, s = heappop(stones), heappop(stones)
            if f < s:
                heappush(stones, f - s)
        try:
            return -stones[0]
        except IndexError:
            return 0


#    def lastStoneWeight(self, stones: List[int]) -> int:
#        while len(stones) > 1:
#            stones.sort()
#            stones.append(stones.pop() - stones.pop())
#        return stones[0]


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(1, [[2, 7, 4, 1, 8, 1]], "lastStoneWeight")
run_test(1, [[1]], "lastStoneWeight")
# run_test(RESULT, [ARGS], 'lastStoneWeight')
