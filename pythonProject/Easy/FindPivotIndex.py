from typing import List

from LogHelper import LogHelper

class FindPivotIndex:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.pivotIndex(nums))

    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        total_sum = sum(nums)
        right_sum = total_sum

        for i, num in enumerate(nums):
            # Efficiently calculate left sum using total_sum and current element
            left_sum = total_sum - num - sum(nums[i + 1:])
            right_sum = right_sum - num
            if left_sum == right_sum:
                return i

        return -1