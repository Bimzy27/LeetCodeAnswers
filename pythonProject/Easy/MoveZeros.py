from typing import List

from LogHelper import LogHelper


class MoveZeros:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.moveZeroes(nums))

    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return None

        i = 0
        popCounter = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                popCounter += 1
                i -= 1
            i += 1

        for i in range(popCounter):
            nums.append(0)

        return None