from LogHelper import LogHelper


class ClimbingStairs:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.climbStairs(n))

    def climbStairs(self, n: int) -> int:
        self.sums = 0
        self.numsDict = dict()

        def climb(n: int) -> int:
            if self.numsDict.__contains__(n):
                self.sums += self.numsDict[n]
            else:
                locSum = 0
                if n == 0:
                    locSum += 1
                    self.sums += 1
                if n >= 2:
                    locSum += climb(n - 2)
                if n >= 1:
                    locSum += climb(n - 1)
                if not self.numsDict.__contains__(n):
                    self.numsDict[n] = locSum
            return self.numsDict[n]

        climb(n)

        return self.sums