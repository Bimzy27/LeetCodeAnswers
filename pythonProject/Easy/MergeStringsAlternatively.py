from LogHelper import LogHelper


class MergeStringsAlternatively:
    def __init__(self, word1: str, word2: str):
        LogHelper.PrintInput(word1)
        LogHelper.PrintInput(word2)
        LogHelper.PrintOutput(self.mergeAlternately(word1, word2))

    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        maxLen = len1 if len1 > len2 else len2
        mergedWord = ''
        for i in range(maxLen):
            if i < len1:
                mergedWord += word1[i]
            if i < len2:
                mergedWord += word2[i]
        return mergedWord
