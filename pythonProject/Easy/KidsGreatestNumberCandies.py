from typing import List
from LogHelper import LogHelper

class KidsGreatestNumberCandies:
    def __init__(self, candies: List[int], extraCandies: int):
        LogHelper.PrintInput(candies)
        LogHelper.PrintInput(extraCandies)
        LogHelper.PrintOutput(self.kidsWithCandies(candies, extraCandies))

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sortedCandies = sorted(candies)
        moreCandyList: List[bool] = []
        for i in range(len(candies)):
            moreCandy: bool = True if (candies[i] + extraCandies) >= sortedCandies[-1] else False
            moreCandyList.append(moreCandy)
        return moreCandyList