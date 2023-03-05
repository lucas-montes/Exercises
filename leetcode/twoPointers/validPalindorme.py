class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_striped_s = [c for c in s.lower() if c.isalnum()]
        backward_striped_s = forward_striped_s[::-1]
        return forward_striped_s == backward_striped_s


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test(True, ["A man, a plan, a canal: Panama"], "isPalindrome")
run_test(False, ["race a car"], "isPalindrome")
run_test(False, ["0P"], "isPalindrome")
