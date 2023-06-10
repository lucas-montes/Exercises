import sys
from typing import List

sys.tracebacklimit = 0


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        combi = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        len_d = len(digits)

        def com(d_index, curr_combi):
            # if our combination is as long as the number of digits
            # it means that we have done all the combinations
            # EX: digits = "23" len = 2 if len curr_combi = 2 means that curr_combi = "ad"
            if len(curr_combi) == len_d:
                result.append(curr_combi)
                return
            for char in combi[digits[d_index]]:
                com(d_index + 1, f"{curr_combi}{char}")

        if digits:
            com(0, "")
        return result

    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        combi = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        to_combi = []
        for d in digits:
            temp = []
            if to_combi:
                for l in to_combi:
                    for cl in combi[d]:
                        temp.append(f"{l}{cl}")
                to_combi = temp
            else:
                to_combi.extend(combi[d])
        return to_combi


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(
    [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ],
    ["23"],
    "letterCombinations",
)
run_test([], [""], "letterCombinations")
run_test(["a", "b", "c"], ["2"], "letterCombinations")
