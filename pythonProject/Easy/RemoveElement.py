from typing import List

from LogHelper import LogHelper


class RemoveElement:
    def __init__(self, nums: List[int], val: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintInput(val)
        LogHelper.PrintOutput(self.removeElement(nums, val))

    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        for i, num in enumerate(reversed(nums)):
            print(i)
            if num == val:
                nums.pop(length - 1 - i)

        print(nums)
        return len(nums)