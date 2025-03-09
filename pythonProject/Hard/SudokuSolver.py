from typing import List

from LogHelper import LogHelper


class SudokuSolver:

    def __init__(self, board: List[List[str]]):
        LogHelper.PrintInput(board)
        LogHelper.PrintOutput(self.solveSudoku(board))

    board: List[List[str]]
    cellIndexPairs = {i: {} for i in range(0, 81)}
    iteration = 0

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.printBoard()
        self.setCellIndexPairs()

    def setCellIndexPairs(self):
        self.iteration += 1
        print(f"Iteration: {self.iteration}")

        filledCell = False
        for index in range(81):
            x = index % 9
            y = int((index - (index % 9)) / 9)
            if self.board[y][x] == '.':
                self.cellIndexPairs[index] = self.getGetPossibleNums(x, y)

        for index in range(81):
            if len(self.cellIndexPairs[index]) == 1:
                filledCell = True
                x = index % 9
                y = int((index - (index % 9)) / 9)
                self.board[y][x] = str(list(self.cellIndexPairs[index])[0])
                self.cellIndexPairs[index] = {}
        self.printBoard()
        if filledCell:
            self.setCellIndexPairs()

    def getGetPossibleNums(self, x: int, y: int) -> set[int]:
        nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        nums = nums.difference(self.getNumsInRow(y))
        nums = nums.difference(self.getNumsInColumn(x))
        nums = nums.difference(self.getNumsInBox(x, y))
        return nums

    def getNumsInRow(self, y: int) -> set[int]:
        nums = set()
        for i in range(9):
            if self.board[y][i] != '.':
                nums.add(int(self.board[y][i]))
        return nums

    def getNumsInColumn(self, x: int) -> set[int]:
        nums = set()
        for i in range(9):
            if self.board[i][x] != '.':
                nums.add(int(self.board[i][x]))
        return nums

    def getNumsInBox(self, x: int, y: int) -> {}:
        nums = set()
        padX = int(x / 3)
        padY = int(y / 3)
        for i in range(3):
            for j in range(3):
                if self.board[(padY * 3) + j][(padX * 3) + i] != '.':
                    nums.add(int(self.board[(padY * 3) + j][(padX * 3) + i]))
        return nums

    def getNum(self, x: int, y: int) -> int:
        return 0 if self.board[y][x] == '.' else int(self.board[y][x])

    def printBoard(self):
        print("=========================================")
        for i, row in enumerate(self.board):
            rowStr = "||"
            for j, cell in enumerate(row):
                rowStr += f" {' ' if cell == '.' else cell} {'||' if (j + 1) % 3 == 0 else '|'}"
            print(rowStr)
            if (i + 1) % 3 == 0:
                print("=========================================")
            else:
                print("-----------------------------------------")
        print()
