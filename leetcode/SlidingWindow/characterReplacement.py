import sys

sys.tracebacklimit = 0


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = {}
        max_len = 0
        max_freq = 0
        for index, letter in enumerate(s):
            seen[letter] = seen.get(letter, 0) + 1

            # we only care about the MAXIMUM of the seen values.
            max_freq = max(max_freq, seen[letter])
            # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
            window_len = index - l + 1

            # if we have replaced <= K letters, record a new max_len
            if window_len - max_freq <= k:
                max_len = max(max_len, window_len)

            # if we have replaced > K letters, then it's time to slide the window
            else:
                # decrement frequency of char at left pointer, then increment left pointer
                seen[s[l]] -= 1
                l += 1

        return max_len


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"


run_test(4, ["ABAB", 2], "characterReplacement")
run_test(4, ["AABABBA", 1], "characterReplacement")
