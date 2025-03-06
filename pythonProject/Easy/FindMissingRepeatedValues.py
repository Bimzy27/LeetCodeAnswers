from typing import List

from LogHelper import LogHelper


class FindMissingRepeatedValues:
    def __init__(self, grid: List[List[int]]):
        LogHelper.PrintInput(grid)
        LogHelper.PrintOutput(self.findMissingAndRepeatedValues(grid))

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nLen = len(grid)
        tot = nLen * nLen
        mydict = {i: 0 for i in range(1, tot+1)}
        for row in grid:
            for value in row:
                mydict[value] += 1
        key_with_value_2 = [key for key, value in mydict.items() if value == 2][0]
        key_with_value_0 = [key for key, value in mydict.items() if value == 0][0]
        return [key_with_value_2, key_with_value_0]