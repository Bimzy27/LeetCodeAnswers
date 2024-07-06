from collections import deque
from typing import List

from pythonProject.LogHelper import LogHelper


class RottingOranges:
    def __init__(self, grid: List[List[int]]):
        LogHelper.PrintInput(grid)
        LogHelper.PrintOutput(self.orangesRotting(grid))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    oranges += 1


        minutes = 0
        consumingOranges = True
        while consumingOranges:
            pendingOranges = []

            while queue:
                row, col = queue.popleft()
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    rowY:int = y + row
                    colX:int = x + col

                    if 0 <= rowY < rows and 0 <= colX < cols and grid[rowY][colX] == 1:
                        pendingOranges.append((rowY, colX))
                        grid[rowY][colX] = 2
                        oranges -= 1

            if len(pendingOranges) > 0:
                minutes += 1
                for row, col in pendingOranges:
                    queue.append((row, col))
            else:
                consumingOranges = False
        if oranges != 0:
            return -1
        return minutes