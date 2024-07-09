from pythonProject.LogHelper import LogHelper


class ClimbingStairs:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.climbStairs(n))

    def climbStairs(self, n: int) -> int:
        sum = 0
        if n >= 2:
            sum += 1
            sum += self.climbStairs(n - 2)
        elif n >= 1:
            sum += 1
            sum += self.climbStairs(n - 1)
        return sum