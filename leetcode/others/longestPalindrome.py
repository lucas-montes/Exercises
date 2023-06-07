import contextlib


class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s != 1 and len_s == 2 and s[0] == s[1] or len_s == 1:
            return s
        elif len_s == 2:
            return s[0]
        return self.manacher(s, len_s)

    def manacher(self, s, N):
        if N == 0:
            return
        N = 2 * N + 1  # Position count
        L = [0] * N
        L[0] = 0
        L[1] = 1
        C = 1  # centerPosition
        R = 2  # centerRightPosition
        i = 0  # currentRightPosition
        iMirror = 0  # currentLeftPosition
        maxLPSLength = 0
        maxLPSCenterPosition = 0
        start = -1
        end = -1
        diff = -1

        # Uncomment it to print LPS Length array
        # printf("%d %d ", L[0], L[1]);
        for i in range(2, N):

            # get currentLeftPosition iMirror for currentRightPosition i
            iMirror = 2 * C - i
            L[i] = 0
            diff = R - i
            # If currentRightPosition i is within centerRightPosition R
            if diff > 0:
                L[i] = min(L[iMirror], diff)

            # Attempt to expand palindrome centered at currentRightPosition i
            # Here for odd positions, we compare characters and
            # if match then increment LPS Length by ONE
            # If even position, we just increment LPS by ONE without
            # any character comparison
            with contextlib.suppress(Exception):
                while ((i + L[i]) < N and (i - L[i]) > 0) and (
                    ((i + L[i] + 1) % 2 == 0)
                    or (s[(i + L[i] + 1) // 2] == s[(i - L[i] - 1) // 2])
                ):
                    L[i] += 1
            if L[i] > maxLPSLength:  # Track maxLPSLength
                maxLPSLength = L[i]
                maxLPSCenterPosition = i

            # If palindrome centered at currentRightPosition i
            # expand beyond centerRightPosition R,
            # adjust centerPosition C based on expanded palindrome.
            if i + L[i] > R:
                C = i
                R = i + L[i]

        # Uncomment it to print LPS Length array
        # printf("%d ", L[i]);
        start = (maxLPSCenterPosition - maxLPSLength) // 2
        end = start + maxLPSLength - 1
        return s[start : end + 1]


assert "s" == Solution().longestPalindrome("so")
assert "a" == Solution().longestPalindrome("a")
assert "bb" == Solution().longestPalindrome("cbbd")
assert "aoa" == Solution().longestPalindrome("aoa")
assert "abcba" == Solution().longestPalindrome("abcba")
assert "aca" == Solution().longestPalindrome("aacabdkacaa")
