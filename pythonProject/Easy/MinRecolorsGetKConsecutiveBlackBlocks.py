from LogHelper import LogHelper


class MinRecolorsGetKConsecutiveBlackBlocks:
    def __init__(self, blocks: str, k: int):
        LogHelper.PrintInput(blocks)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.minimumRecolors(blocks, k))

    def minimumRecolors(self, blocks: str, k: int) -> int:
        bLen = len(blocks)
        min = k

        if bLen == min:
            return min

        for i in range(bLen - k):
            count = 0
            for j in range(k):
                if blocks[i + j] == "W":
                    count += 1
            if count < min:
                min = count
        return min