from typing import List

from LogHelper import LogHelper


class MaxNumberKSumPairs:
    def __init__(self, nums: List[int], k: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.maxOperations(nums, k))

    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        ops: int = 0

        for i in range(len(nums)):
            n = nums[i]
            if n < k:
                if n in dic:
                    dic[n] += 1
                else:
                    dic[n] = 1

        for key, value in dic.items():
            other = k - key
            #key is self
            if other == key:
                ops += int(value / 2)
                dic[key] = 0
            elif other in dic and dic[other] > 0:
                ops += value if value < dic[other] else dic[other]
                dic[other] = 0
                dic[key] = 0

        return ops