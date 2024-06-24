from typing import List

from LogHelper import LogHelper


class EqualRowColumnPairs:
    def __init__(self, grid: List[List[int]]):
        LogHelper.PrintInput(grid)
        LogHelper.PrintOutput(self.equalPairs(grid))

    def get_key(self, nums:List[int]) -> str:
        key = ""
        for i, num in enumerate(nums):
            if i != 0:
                key += ','
            key += str(num)
        print('Key: ' + key)
        return key

    def get_column(self, grid: List[List[int]], index: int) -> List[int]:
        length = len(grid)
        column = []
        for i in range(length):
            column.append(grid[i][index])
        return column

    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        grids = {}

        for i, nums in enumerate(grid):
            key = self.get_key(nums)
            value = rows.get(key, 0)
            rows[key] = value + 1

            nums2 = self.get_column(grid, i)
            key = self.get_key(nums2)
            value = grids.get(key, 0)
            grids[key] = value + 1
        print(rows)
        print(grids)

        count = 0
        for key in rows:
            if grids.__contains__(key):
                count += rows[key] * grids[key]
        return count

