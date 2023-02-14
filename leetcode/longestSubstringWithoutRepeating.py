def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    current_index_char = {}
    i = 0
    # try to extend the range [i, j]
    for j in range(len(s)):
        if s[j] in current_index_char:
            i = max(current_index_char[s[j]], i)

        ans = max(ans, j - i + 1)
        current_index_char[s[j]] = j + 1

    return ans
