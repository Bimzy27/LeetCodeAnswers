from typing import List

from LogHelper import LogHelper


class ContainerWithMostWater:
    def __init__(self, height: List[int]):
        LogHelper.PrintInput(height)
        LogHelper.PrintOutput(self.maxArea(height))

    def maxArea(self, height: List[int]) -> int:
        indexFirst = 0
        indexLast = len(height) - 1
        maxArea:int = 0

        while indexFirst < indexLast:
            f = height[indexFirst]
            l = height[indexLast]
            d = indexLast - indexFirst
            m = f if f < l else l

            if d*m > maxArea:
                maxArea = d*m

            if f <= l:
                indexFirst += 1
            else:
                indexLast -= 1

        return maxArea