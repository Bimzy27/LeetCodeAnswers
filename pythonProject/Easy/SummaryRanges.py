from typing import List

from LogHelper import LogHelper


class SummaryRanges:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.summaryRanges(nums))

    def summaryRanges(self, nums: List[int]) -> List[str]:
        numsL = len(nums)
        if numsL == 0:
            return []

        ranges = []
        l = nums[0]
        r = l

        for i in range(numsL):
            if nums[i] - r > 1:
                if l == r:
                    ranges.append(f"{l}")
                else:
                    ranges.append(f"{l}->{r}")
                l = nums[i]
            r = nums[i]

        if l == r:
            ranges.append(f"{l}")
        else:
            ranges.append(f"{l}->{r}")

        return ranges
