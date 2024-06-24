class ZigZagConversion:
    def __init__(self, s: str, numRows: int):
        print(f"{s} - Input, Rows: {numRows}")
        self.convert(s, numRows)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        count = len(s) + 1 if len(s) < numRows else numRows
        emptyStrList = []
        for i in range(count):
            emptyStrList.append('')
        sOut = ''
        columnList = []
        zig = True
        zigCounter = 0

        for i in range(len(s)):
            if zig:
                if zigCounter == 0:
                    columnList.append(emptyStrList.copy())
                columnList[-1][zigCounter] = s[i]
                zigCounter += 1
                if zigCounter == count:
                    if count == 2:
                        zigCounter = 0
                    else:
                        zigCounter = count - 1
                        zig = False
            else:
                zigCounter -= 1
                zagList = emptyStrList.copy()
                zagList[zigCounter] = s[i]
                columnList.append(zagList)
                if zigCounter == 1:
                    zigCounter = 0
                    zig = True


        for i in range(count):
            for j in range(len(columnList)):
                sOut += columnList[j][i]

        #print(columnList)
        print(f"{sOut} - Output")
        return sOut