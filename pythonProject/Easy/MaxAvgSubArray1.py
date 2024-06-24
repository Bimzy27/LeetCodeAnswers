from typing import List

from LogHelper import LogHelper


class MaxAvgSubArray1:
    def __init__(self, nums: List[int], k: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.findMaxAverage(nums, k))

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        avg: float = 0
        if n <= k:
            for num in nums:
                avg += num
            avg /= k
            return avg
        counter:int = 0
        for i in range(k):
            counter += nums[i]

        avg = counter / k
        minI = 0
        maxI = k - 1

        while maxI < len(nums):
            if maxI - minI >= k:
                counter -= nums[minI]
                minI += 1
                l_avg = counter / k
                if l_avg > avg:
                    avg = l_avg
            else:
                l_avg = counter / k
                if l_avg > avg:
                    avg = l_avg
                maxI += 1
                if maxI < len(nums):
                    counter += nums[maxI]

        return avg