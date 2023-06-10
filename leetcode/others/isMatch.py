import sys
from typing import List

sys.tracebacklimit = 0


class TrieNode:
    def __init__(self):
        self.child: dict = {}
        self.end: bool = False


class WDic:
    """
    Tree implementation
    """

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def add_word(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.child.setdefault(letter, TrieNode())
        current.end = True

    def next_is_star(self, index, word):
        try:
            next_char = word[index + 1]
        except IndexError:
            next_char = ""
        return next_char == "*"

    def search(self, word: str, root=None) -> bool:
        current = root or self.root
        if word == ".*":
            return True

        l = 0
        while l < len(word):
            cur_char = word[l]
            is_star = self.next_is_star(l, word)
            if cur_char == ".":
                l += 2 if is_star else 1
                for values in current.child.values():
                    if self.search(word[l:], values):
                        return True
            if is_star:
                try:
                    current = current.child[cur_char]
                except KeyError:
                    l += 2
            else:
                try:
                    current = current.child[cur_char]
                    l += 1
                except KeyError:
                    return False

        return current.end


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = WDic()
        r.add_word(s)
        return r.search(p)


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert (
        expected == result
    ), f"at test with params {test_data} result is {result} and the expected value: {expected}"
    print(f"{expected} success ✅")


run_test(False, ["aa", "a"], "isMatch")
run_test(True, ["aa", "a*"], "isMatch")
run_test(True, ["ab", ".*"], "isMatch")
run_test(True, ["aab", "c*a*b"], "isMatch")
run_test(True, ["aaa", "a*a"], "isMatch")
https: // leetcode.com/problems/regular-expression-matching /?envType = featured-list & envId = top-interview-questions
