from typing import List

from LogHelper import LogHelper


class CombinationSumIII:
    def __init__(self, k: int, n: int):
        LogHelper.PrintInput(k)
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.combinationSum3(k, n))

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []
        def backtrack(nums, i):
            if len(nums) == k:
                nSum = sum(nums)
                if nSum == n:
                    nums = sorted(nums)
                    out.append(nums)
                elif nSum < n:
                    backtrack(nums[:k - 1], i)
            else:
                for j in range(9 - i):
                    backtrack(nums, j+i)
                nums.append(i)
                backtrack(nums, i + 1)

            backtrack([], i+1)

        return out