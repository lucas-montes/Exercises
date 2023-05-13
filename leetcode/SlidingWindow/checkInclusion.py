import sys
from collections import Counter
from typing import List

sys.tracebacklimit = 0


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, matches = Counter(s1), 0
        len_s1 = len(s1)
        for index, letter in enumerate(s2):
            # check the new letter
            if letter in cntr:
                cntr[letter] -= 1
                if cntr[letter] == 0:
                    matches += 1

            # Subtract left
            if index + 1 > len_s1:
                if (left := s2[index - len_s1]) in cntr:
                    cntr[left] += 1
                    # means it came to 1 from 0
                    if cntr[left] == 1:
                        matches -= 1

            if matches == len(cntr):
                return True

        return False


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(True, ["ab", "eidbaooo"], "checkInclusion")
run_test(False, ["ab", "eidboaoo"], "checkInclusion")
run_test(True, ["ab", "ab"], "checkInclusion")
