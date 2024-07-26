from typing import List

from LogHelper import LogHelper


class CombinationSumIII:
    def __init__(self, k: int, n: int):
        LogHelper.PrintInput(k)
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.combinationSum3(k, n))

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []
        def backtrack(nums, next: int):
            if nums.__contains__(next):
                return
            nums.append(next)
            if len(nums) >= k:
                if sum(nums) == n:
                    nums.sort()
                    if not out.__contains__(nums):
                        out.append(nums)
                return
            for i in range(9):
                backtrack(nums.copy(), i + 1)

        for i in range(9):
            backtrack([], i + 1)

        return out