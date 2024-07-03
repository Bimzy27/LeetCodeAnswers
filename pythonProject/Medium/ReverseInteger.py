from LogHelper import LogHelper


class ReverseInteger:
    def __init__(self, x: int):
        LogHelper.PrintInput(x)
        LogHelper.PrintOutput(self.reverse(x))

    def reverse(self, x: int) -> int:
        numStr = str(x)
        revStr = ""
        for char in numStr:
            if char.isdigit():
                revStr = char + revStr
        if numStr[0] == "-":
            revStr = "-"+revStr

        revNum = int(revStr)
        if revNum > 2147483647:
            return 0
        elif revNum < -2147483647:
            return 0
        return revNum