from typing import List

# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        if n == 0:
            return [""]
        result = []
        for index in range(n):
            for left in self.generateParenthesis(c):
                result.extend(
                    f"({left}){right}"
                    for right in self.generateParenthesis(n - 1 - index)
                )
        return result


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test(["()"], 1, "generateParenthesis")
run_test(["()()", "(())"], 2, "generateParenthesis")
run_test(["((()))", "(()())", "(())()", "()(())", "()()()"], 3, "generateParenthesis")
