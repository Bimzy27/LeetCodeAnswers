from pythonProject.LogHelper import LogHelper


class LengthLastWord:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.lengthOfLastWord(s))

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])