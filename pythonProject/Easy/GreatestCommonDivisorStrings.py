from LogHelper import LogHelper


class GreatestCommonDivisorStrings:
    def __init__(self, str1: str, str2: str):
        LogHelper.PrintInput(str1)
        LogHelper.PrintInput(str2)
        LogHelper.PrintOutput(self.gcdOfStrings(str1, str2))

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        len1 = len(str1)
        len2 = len(str2)
        lenMax = len1 if len1 < len2 else len2
        commonStr = str1 if len1 < len2 else str2
        for i in range(lenMax):
            divStr1 = str1
            while divStr1.startswith(commonStr):
                divStr1 = divStr1[len(commonStr):]
            divStr2 = str2
            while divStr2.startswith(commonStr):
                divStr2 = divStr2[len(commonStr):]
            if divStr1 == '' and divStr2 == '':
                return commonStr
            else:
                commonStr = commonStr[:-1]
        return commonStr