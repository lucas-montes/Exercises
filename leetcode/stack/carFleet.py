import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a car's position is always < than target at the start,
        # so it's fine to start curtime at 0 (no fleet will be at target at time 0)
        fleets = curtime = 0
        # we reverse the sorted list so we start for the car at the top position
        # this will allow us to know what is the top speed as the ones after wont
        # be able to go faster
        for p, s in sorted(zip(position, speed), reverse=True):
            destination_time = (target - p) / s
            if curtime < destination_time:
                fleets += 1
                curtime = destination_time

        return fleets


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(3, [12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]], "carFleet")
run_test(1, [100, [0, 2, 4], [4, 2, 1]], "carFleet")
run_test(1, [10, [3], [3]], "carFleet")
