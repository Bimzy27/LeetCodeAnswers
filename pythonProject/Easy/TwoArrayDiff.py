from typing import List

from LogHelper import LogHelper


class TwoArrayDiff:
    def __init__(self, nums1: List[int], nums2: List[int]):
        LogHelper.PrintInput(nums1)
        LogHelper.PrintInput(nums2)
        LogHelper.PrintOutput(self.findDifference(nums1, nums2))

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert lists to sets for efficient lookups
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        # Find the difference using set operations
        difference_nums1 = list(set_nums1 - set_nums2)  # Elements in nums1 but not nums2
        difference_nums2 = list(set_nums2 - set_nums1)  # Elements in nums2 but not nums1

        # Combine the differences into a single list
        return [difference_nums1, difference_nums2]
