from typing import List

from LogHelper import LogHelper


class HouseRobber:
    def __init__(self, nums):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.rob(nums))

    def rob(self, nums: List[int]) -> int:
        nLen = len(nums)

        if nLen == 1:
            return nums[0]

        nums[1] = max(nums[0], nums[1])

        for i in range(2, nLen):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        return nums[-1]