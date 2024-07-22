from typing import List

from LogHelper import LogHelper


class BuySellStock:
    def __init__(self, prices: List[int]):
        LogHelper.PrintInput(prices)
        LogHelper.PrintOutput(self.maxProfit(prices))

    def maxProfit(self, prices: List[int]) -> int:

        def backtrack(nums) -> int:
            if len(nums) <= 1:
                return 0
            maxi = 0
            for i, n in enumerate(nums[:-1]):
                if nums[-1] - n > maxi:
                    maxi = nums[-1] - n
            maxi = max(maxi, backtrack(nums[:-1]))
            return maxi

        return backtrack(prices)