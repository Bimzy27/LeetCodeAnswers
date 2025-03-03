from typing import List

from LogHelper import LogHelper


class MissingNumber:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.missingNumber(nums))

    def missingNumber(self, nums: List[int]) -> int:
        nLen = len(nums)
        sortedNums = sorted(nums)
        for i in range(nLen):
            if sortedNums[i] != i:
                return i
        return nLen
