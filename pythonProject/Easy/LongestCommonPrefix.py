from typing import List

from LogHelper import LogHelper


class LongestCommonPrefix:
    def __init__(self, strs: List[str]):
        LogHelper.PrintInput(strs)
        LogHelper.PrintOutput(self.longestCommonPrefix(strs))

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        length = len(strs)
        while True:
            index = len(prefix)

            if index >= len(strs[0]):
                return prefix

            for i in range(1, length):
                if index >= len(strs[i]):
                    return prefix

                if strs[i][index] != strs[0][index]:
                    return prefix
            prefix += strs[0][index]
