import sys

sys.tracebacklimit = 0


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if s == t:
            return s

        start_index, end_index = None, None

        to_see = {}
        have, l, need = 0, 0, len(set(t))
        for lett in t:
            to_see[lett] = to_see.get(lett, 0) + 1

        seen = {}
        length = float("infinity")

        for index, right_letter in enumerate(s):
            seen[right_letter] = seen.get(right_letter, 0) + 1

            if right_letter in to_see and seen[right_letter] == to_see[right_letter]:
                have += 1

            while have == need:
                new_length = index - l + 1
                if length > new_length:
                    start_index = l
                    end_index = index
                    length = new_length

                left_letter = s[l]
                seen[left_letter] -= 1
                if left_letter in to_see and seen[left_letter] < to_see[left_letter]:
                    have -= 1

                l += 1

        return s[start_index : end_index + 1] if length != float("infinity") else ""


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test("BANC", ["ADOBECODEBANC", "ABC"], "minWindow")
run_test("a", ["a", "a"], "minWindow")
run_test("", ["a", "aa"], "minWindow")
run_test("aa", ["aa", "aa"], "minWindow")
run_test("baa", ["bbaa", "aba"], "minWindow")
