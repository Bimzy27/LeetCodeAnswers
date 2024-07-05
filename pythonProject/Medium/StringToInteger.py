from LogHelper import LogHelper


class StringToInteger:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.myAtoi(s))

    def myAtoi(self, s: str) -> int:
        consumedNum = False
        consumedSign = False
        isNegative = False
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                consumedSign = True
                consumedNum = True
                n = int(s[i])
                if num == 0:
                    num = n
                else:
                    num *= 10
                    num += n
            elif not consumedSign and s[i] == "-":
                consumedSign = True
                consumedNum = True
                isNegative = True
            elif not consumedSign and s[i] == "+":
                consumedSign = True
                consumedNum = True
            elif consumedNum and s[i] == " ":
                break
            elif s[i] != " ":
                break
        if isNegative:
            num *= -1

        min_value = -2 ** 31  # Minimum value for int32
        max_value = 2 ** 31 - 1  # Maximum value for int32 (inclusive)
        num = max(min_value, min(num, max_value))

        return num
