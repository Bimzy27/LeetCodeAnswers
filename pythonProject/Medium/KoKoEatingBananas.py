import math
from typing import List

from LogHelper import LogHelper


class KoKoEatingBananas:
    def __init__(self, piles: List[int], h: int):
        LogHelper.PrintInput(piles)
        LogHelper.PrintInput(h)
        LogHelper.PrintOutput(self.minEatingSpeed(piles, h))

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        count = r

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for num in piles:
                hours += math.ceil(num / mid)
            if hours <= h:
                count = min(count, mid)
                r = mid - 1
            else:
                l = mid + 1

        return count