from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = int(float("inf"))
        for price in prices:
            min_price = min(min_price, price)
            curr_profit = price - min_price
            profit = max(curr_profit, profit)
        return profit
