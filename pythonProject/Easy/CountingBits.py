from typing import List

from LogHelper import LogHelper


class CountingBits:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.countBits(n))

    def countOnesInBinary(self, number: int):
        count = 0
        while number:
            count += number & 1  # Check the least significant bit
            number >>= 1  # Right shift the number by 1 bit
        return count

    def countBits(self, n: int) -> List[int]:
        bitNums = []
        for i in range(n + 1):
            LogHelper.Print(i)
            bitNums.append(self.countOnesInBinary(i))
        return bitNums