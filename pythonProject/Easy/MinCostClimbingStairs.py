from typing import List

from LogHelper import LogHelper


class MinConstClimbingStairs:
    def __init__(self, cost: List[int]):
        LogHelper.PrintInput(cost)
        LogHelper.PrintOutput(self.minCostClimbingStairs(cost))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)

        def minCost(n):
            if n < 2:
                return cost[n]

            return cost[n] + min(minCost(n - 1), minCost(n - 2))

        return min(minCost(length - 1), minCost(length - 2))