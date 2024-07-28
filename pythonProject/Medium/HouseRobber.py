from typing import List

from LogHelper import LogHelper


class HouseRobber:
    def __init__(self, nums):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.rob(nums))

    def rob(self, nums: List[int]) -> int:
        