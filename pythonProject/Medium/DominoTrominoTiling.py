from LogHelper import LogHelper


class DominoTrominoTiling:
    def __init__(self, n: int):
        LogHelper.PrintInput(n)
        LogHelper.PrintOutput(self.numTilings(n))

    def numTilings(self, n: int) -> int:
        full, top, bottom = {0: 1, 1: 1}, {1: 0}, {1: 0}

        for i in range(2, n+1):
            full[i] = full[i - 1] + full[i - 2] + top[i - 1] + bottom[i - 1]
            top[i] = bottom[i - 1] + full[i - 2]
            bottom[i] = top[i - 1] + full[i - 2]

        return full[n] % (10**9 + 7)