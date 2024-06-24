from typing import List

from LogHelper import LogHelper


class MaxConsecutiveOnes:
    def __init__(self, nums: List[int], k: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.longestOnes(nums, k))

    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        thisK = 0
        longest = 0
        length = len(nums)

        while start < length - 1:
            if end < length and nums[end] == 1:
                end += 1
            elif end < length and nums[end] == 0 and thisK < k:
                thisK += 1
                end += 1
            else:
                if nums[start] == 0:
                    start += 1
                    thisK -= 1
                elif nums[start] == 1:
                    start += 1

            if end - start > longest:
                longest = end - start

        return longest
