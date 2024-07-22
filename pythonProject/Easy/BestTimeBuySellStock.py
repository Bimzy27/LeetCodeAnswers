from typing import List

from LogHelper import LogHelper


class BuySellStock:
    def __init__(self, prices: List[int]):
        LogHelper.PrintInput(prices)
        LogHelper.PrintOutput(self.maxProfit(prices))

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit