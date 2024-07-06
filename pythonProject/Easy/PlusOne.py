from typing import List

from pythonProject.LogHelper import LogHelper


class PlusOne:
    def __init__(self, digits: List[int]):
        LogHelper.PrintInput(digits)
        LogHelper.PrintOutput(self.plusOne(digits))

    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            if i > 0:
                num *= 10
            num += digits[i]

            print(num)
        num += 1
        nums = []
        for c in str(num):
            nums.append(int(c))
        return nums