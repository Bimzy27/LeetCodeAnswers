from LogHelper import LogHelper


class CountTotalNumberColoredCells:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.coloredCells(n))

    def coloredCells(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        nums = []
        for i in range(n - 1):
            num = (i * 2) + 1
            if 1 > 0:
                num += nums[i - 1]
            nums.append(num)
        return (nums[len(nums) - 1] * 2) + ((n - 1) * 2) + 1