from collections import deque
from typing import List

from LogHelper import LogHelper


class NearestExitFromMazeEntrance:
    def __init__(self, maze: List[List[str]], entrance: List[int]):
        LogHelper.PrintInput(maze)
        LogHelper.PrintInput(entrance)
        LogHelper.PrintOutput(self.nearestExit(maze, entrance))

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            row, col, count = queue.popleft()

            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                rowY = y + row
                colX = x + col

                if 0 <= rowY < rows and 0 <= colX < cols and maze[rowY][colX] == ".":
                    if (rowY == 0 or rowY == rows - 1) or (colX == 0 or colX == cols - 1):
                        return count + 1
                    maze[rowY][colX] = "+"
                    queue.append((rowY, colX, count + 1))

        return -1