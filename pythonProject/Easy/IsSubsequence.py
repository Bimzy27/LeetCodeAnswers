from LogHelper import LogHelper


class IsSubsequence:
    def __init__(self, s: str, t: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintInput(t)
        LogHelper.PrintOutput(self.isSubsequence(s, t))

    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        if len(s) > len(t):
            return False

        counter = 0
        sIndex = s[counter]

        for i in range(len(t)):
            if t[i] == sIndex:
                counter += 1
                sIndex = s[counter]

        return counter == len(s)