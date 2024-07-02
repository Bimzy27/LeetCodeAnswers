from LogHelper import LogHelper


class RomanToInteger:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.romanToInt(s))

    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        table = {
            'I' : 1,
            'IV' : 4,
            'V' : 5,
            'IX' : 9,
            'X' : 10,
            'XL' : 40,
            'L' : 50,
            'XC' : 90,
            'C' : 100,
            'CD' : 400,
            'D' : 500,
            'CM' : 900,
            'M' : 1000,
        }

        sum = 0
        while len(s) > 1:
            if table.__contains__(s[:2]):
                sum += table[s[:2]]
                s = s[2:]
            else:
                sum += table[s[:1]]
                s = s[1:]
            print(s)

        if len(s) > 0:
            sum += table[s]
        return sum