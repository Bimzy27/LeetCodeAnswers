from typing import List

from LogHelper import LogHelper


class SearchInsertPosition:
    def __init__(self, nums: List[int], target: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintInput(target)
        LogHelper.PrintOutput(self.searchInsert(nums, target))

    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)