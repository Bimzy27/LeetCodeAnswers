from pythonProject.LogHelper import LogHelper


class AddBinary:
    def __init__(self, a: str, b: str):
        LogHelper.PrintInput(a)
        LogHelper.PrintInput(b)
        LogHelper.PrintOutput(self.addBinary(a, b))
    def addBinary(self, a: str, b: str) -> str:
        num = int(a, 2) + int(b, 2)
        return str(bin(num)[2:])