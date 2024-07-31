from LogHelper import LogHelper


class MinFlipsMakeAOrBEqualC:
    def __init__(self, a: int, b: int, c: int):
        LogHelper.PrintInput(a)
        LogHelper.PrintInput(b)
        LogHelper.PrintInput(c)
        LogHelper.PrintOutput(self.minFlips(a, b, c))

    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while c > 0 or a > 0 or b > 0:
            if c % 2 == 0:
                if a % 2 == 1:
                    count += 1
                if b % 2 == 1:
                    count += 1
            elif a % 2 == 0 and b % 2 == 0:
                count += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return count

