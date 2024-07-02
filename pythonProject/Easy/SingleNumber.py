from typing import List

from LogHelper import LogHelper


class SingleNumber:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.singleNumber(nums))

    def singleNumber(self, nums: List[int]) -> int:
        numsSorted = sorted(nums)

        for i, num in enumerate(numsSorted):
            if i % 2 == 0:
                continue
            if numsSorted[i - 1] == num:
                continue
            return numsSorted[i - 1]

        return numsSorted[-1]
