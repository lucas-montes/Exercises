from typing import List

# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def par_around_one(self, n):
        par_left = n
        while par_left > 0:
            res = "(" * par_left + ")" * par_left
            par_left -= 1

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n == 1:
            return ["()"]
        easy_1 = "()" * n
        easy_2 = "(" * n + ")" * n
        return [easy_1, easy_2]


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test(["()"], 1, "generateParenthesis")
run_test(["()()", "(())"], 2, "generateParenthesis")
run_test(["((()))", "(()())", "(())()", "()(())", "()()()"], 3, "generateParenthesis")
