from typing import List

from LogHelper import LogHelper


class NearestExitFromMazeEntrance:
    def __init__(self, maze: List[List[str]], entrance: List[int]):
        LogHelper.PrintInput(maze)
        LogHelper.PrintInput(entrance)
        LogHelper.PrintOutput(self.nearestExit(maze, entrance))

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [False] * (len(maze) * len(maze[0]))

        def neighbours(i) -> List[int]:
            neibs = []

            x = int(i % 4)
            y = int(i / 4)

            def tryAdd(x, y):
                if x >= 0 and x < len(maze[0]) and y >= 0 and y < len(maze):
                    neibs.append((y * 4) + x)

            tryAdd(x + 1, y)
            tryAdd(x, y + 1)
            tryAdd(x - 1, y)
            tryAdd(x, y - 1)

            print(neibs)

            return neibs

        def visit(i):
            visited[i] = True

        def onEdge(i) -> bool:
            x = int(i % 4)
            y = int(i / 4)
            return maze[y][x] == "." and x == 0 and x == len(maze[0]) - 1 and y == 0 and y == len(maze) - 1

        self.shortest = -1
        def bfs(i):
            queue = [i]
            while len(queue) > 0:
                ij = queue.pop(0)
                travel = 0
                if not visited[i]:
                    visit(i)
                    travel += 1
                    for j, num in enumerate(neighbours(i)):
                        if not visited[j]:
                            queue.append(j)
                            self.shortest = max(travel, self.shortest)
                            if onEdge(j):
                                break

        bfs((entrance[0] * 4) + entrance[1])

        return self.shortest