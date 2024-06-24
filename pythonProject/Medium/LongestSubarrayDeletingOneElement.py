from typing import List

from LogHelper import LogHelper


class LongestSubarrayDeletingOneElement:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.longestSubarray(nums))

    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        longest = 0
        length = len(nums)
        zeroConsumed = False

        while start < length:
            if end < length and nums[end] == 1:
                end += 1
            elif end < length and nums[end] == 0 and zeroConsumed is False:
                end += 1
                zeroConsumed = True
            else:
                if nums[start] == 0:
                    start += 1
                    zeroConsumed = False
                elif nums[start] == 1:
                    start += 1

            if end - start - 1 > longest and zeroConsumed:
                longest = end - start - 1
            elif end - start > longest and zeroConsumed is False:
                longest = end - start

            if longest == length:
                return longest - 1

        return longest
