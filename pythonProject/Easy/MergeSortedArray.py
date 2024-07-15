from typing import List

from LogHelper import LogHelper


class MergeSortedArray:
    def __init__(self, nums1: List[int], m: int, nums2: List[int], n: int):
        LogHelper.PrintInput(nums1)
        LogHelper.PrintInput(m)
        LogHelper.PrintInput(nums2)
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.merge(nums1, m, nums2, n))

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums = []
        nums += nums1[:m]
        nums += nums2[:n]
        nums.sort()
        for i, num in enumerate(nums):
            nums1[i] = num
