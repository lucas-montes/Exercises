from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        max_profit = 0
        l, r = 0, 1
        while r < len_prices:
            buy_price = prices[l]
            sell_price = prices[r]
            if buy_price > sell_price:
                l += 1
            else:
                current_profit = sell_price - buy_price
                if current_profit > max_profit:
                    max_profit = current_profit
                r += 1

        return max_profit


def run_test(expected, test_data, method):
    result = getattr(Solution(), method)(*test_data)
    assert expected == result, f"result is {result} and the expected value: {expected}"


run_test(5, [[7, 1, 5, 3, 6, 4]], "maxProfit")
run_test(0, [[7, 6, 4, 3, 1]], "maxProfit")
run_test(1, [[1, 2]], "maxProfit")
run_test(2, [[2, 1, 2, 1, 0, 1, 2]], "maxProfit")
