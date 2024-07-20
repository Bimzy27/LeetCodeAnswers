from typing import List

from LogHelper import LogHelper


class PascalsTriangle:
    def __init__(self, numRows: int):
        LogHelper.PrintInput(numRows)
        LogHelper.PrintOutput(self.generate(numRows))

    def generate(self, numRows: int) -> List[List[int]]:
        rows: List[List[int]] = []
        for i in range(numRows):
            row: List[int] = [1 for _ in range(i + 1)]
            rows.append(row)

            if i > 1:
                for j in range(i - 1):
                    row[j + 1] = rows[i - 1][j] + rows[i - 1][j + 1]

        return rows

class PascalsTriangleII:
    def __init__(self, rowIndex: int):
        LogHelper.PrintInput(rowIndex)
        LogHelper.PrintOutput(self.getRow(rowIndex))

    def getRow(self, rowIndex: int) -> List[int]:
        rows: List[List[int]] = []
        for i in range(rowIndex + 1):
            row: List[int] = [1 for _ in range(i + 1)]
            rows.append(row)

            if i > 1:
                for j in range(i - 1):
                    row[j + 1] = rows[i - 1][j] + rows[i - 1][j + 1]

        return rows[-1]