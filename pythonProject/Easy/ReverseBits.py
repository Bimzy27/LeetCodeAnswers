from LogHelper import LogHelper


class ReverseBits:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.reverseBits(n))

    def reverseBits(self, n: int) -> int:
        binstr = str(bin(n))
        revstr = binstr[::-1]
        revstr = revstr[:-2]
        for i in range(32 -len(revstr)):
            revstr += '0'
        result = int(revstr, 2)
        return result