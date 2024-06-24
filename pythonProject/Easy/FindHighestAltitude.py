from typing import List

from LogHelper import LogHelper


class FindHighestAltitude:
    def __init__(self, gain: List[int]):
        LogHelper.PrintInput(gain)
        LogHelper.PrintOutput(self.largestAltitude(gain))

    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        hAlt = 0

        for i in range(len(gain)):
            alt += gain[i]
            hAlt = alt if alt > hAlt else hAlt

        return hAlt