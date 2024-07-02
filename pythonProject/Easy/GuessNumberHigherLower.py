from LogHelper import LogHelper


class GuessNumberHigherLower:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.guessNumber(n))

    def guess(self, num: int) -> int:
        return 0

    def guessNumber(self, n: int) -> int:
        return self.binarySearch(1, n)

    def binarySearch(self, low, high):
        mid = (low + high) // 2
        if self.guess(mid) == 0:
            return mid
        if self.guess(mid) == 1:
            return self.binarySearch(mid+1, high)
        if self.guess(mid) == -1:
            return self.binarySearch(low, mid-1)