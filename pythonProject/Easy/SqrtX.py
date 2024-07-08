from LogHelper import LogHelper


class SqrtX:
    def __init__(self, x: int):
        LogHelper.PrintInput(x)
        LogHelper.PrintOutput(self.mySqrt(x))

    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l < r:
            m = (l + r) // 2
            if m*m < x:
                l = m + 1
            elif m*m > x:
                r = m - 1

        return r
