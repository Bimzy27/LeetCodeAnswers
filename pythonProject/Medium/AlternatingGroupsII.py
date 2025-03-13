from typing import List

from LogHelper import LogHelper

class AlternatingGroupsII:
    def __init__(self, colors: List[int], k: int):
        LogHelper.PrintInput(colors)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.numberOfAlternatingGroups(colors, k))

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        padL = int(k / 2) if k % 2 == 0 else int(k / 2) + 1
        padR = int(k / 2)
        last_two = colors[-padL:]
        first_two = colors[:padR]
        colors = last_two + colors + first_two
        cLen = len(colors)
        l = 0
        r = 0
        count = 0
        for i in range(cLen):
            if r + 1 < cLen:
                if colors[r] == colors[r + 1]:
                    if r - l >= k:
                        count += r - l - (k - 1)
                        print(f"1 - c: {count}, l: {l}, r: {r}")
                    l = i
                r = i + 1
            elif r - l >= k - 1:
                count += r - l - (k - 1)
                print(f"2 - c: {count}, l: {l}, r: {r}")
        return count