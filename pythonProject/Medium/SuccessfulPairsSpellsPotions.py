import math
import bisect
from typing import List

from LogHelper import LogHelper


class SuccessfulPairsSpellsPotions:
    def __init__(self, spells: List[int], potions: List[int], success: int):
        LogHelper.PrintInput(spells)
        LogHelper.PrintInput(potions)
        LogHelper.PrintInput(success)
        LogHelper.PrintOutput(self.successfulPairs(spells, potions, success))

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sPots = sorted(potions)
        spellsLen = len(spells)
        results = []
        for i in range(spellsLen):
            x = math.ceil(success / spells[i])
            j = bisect.bisect_left(sPots, x)
            results.append(len(sPots) - j)
        return results