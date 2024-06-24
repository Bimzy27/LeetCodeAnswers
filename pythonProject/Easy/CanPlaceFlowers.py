from typing import List

from LogHelper import LogHelper


class CanPlaceFlowers:
    def __init__(self, flowerbed: List[int], n: int):
        LogHelper.PrintInput(flowerbed)
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.canPlaceFlowers(flowerbed, n))

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowersCount = len(flowerbed)
        for i in range(flowersCount):
            if flowerbed[i] == 1:
                continue
            if i != 0 and flowerbed[i - 1] == 1:
                continue
            if i != flowersCount - 1 and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            n -= 1
            if n <= 0:
                return True
        return False