from typing import List

from LogHelper import LogHelper


class FindPeakElement:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.findPeakElement(nums))

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + right >> 1

            if nums[mid - 1] <= nums[mid] >= nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
