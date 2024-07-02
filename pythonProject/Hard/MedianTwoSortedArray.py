from typing import List

from LogHelper import LogHelper


class MedianTwoSortedArray:
    def __init__(self, nums1: List[int], nums2: List[int]):
        LogHelper.PrintInput(nums1)
        LogHelper.PrintInput(nums2)
        LogHelper.PrintOutput(self.findMedianSortedArrays(nums1, nums2))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        print(nums)
        if length % 2 == 0:
            mid = length / 2
            return (nums[int(mid - 1)] + nums[int(mid)]) / 2

        return nums[int((length - 1) / 2)]