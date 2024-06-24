import sys
from typing import List
from LogHelper import LogHelper


class IncreasingTripletSubsequence:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.increasingTriplet(nums))

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(len(nums) - 2):
            mid = sys.maxsize
            max = sys.maxsize
            min = sys.maxsize
            for j in range(len(nums) - i):
                if nums[i + j] < min:
                    min = nums[i + j]
                elif nums[i + j] < mid and nums[i + j] > min:
                    mid = nums[i + j]
                elif nums[i + j] < max and nums[i + j] > mid:
                    max = nums[i + j]

                if min < mid < max and min != sys.maxsize and mid != sys.maxsize and max != sys.maxsize:
                    return True

        return False
