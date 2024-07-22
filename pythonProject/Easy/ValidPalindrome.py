from LogHelper import LogHelper


class ValidPalindrome:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.isPalindrome(s))

    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for c in s:
            if c.isnumeric() or c.isalpha():
                s2 += c.lower()
        length = len(s2)
        half = length // 2
        for i in range(half):
            if s2[i] != s2[-(i + 1)]:
                return False
        return True