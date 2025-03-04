from typing import List

from LogHelper import LogHelper


class ContainsDuplicateII:
    def __init__(self, nums: List[int], k: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.containsNearbyDuplicate(nums, k))

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        nearby = []
        for i in range(len(nums)):
            if len(nearby) > k:
                nearby.pop(0)

            if nearby.__contains__(nums[i]):
                return True
            nearby.append(nums[i])
        return False


