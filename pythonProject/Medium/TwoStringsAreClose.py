from itertools import islice

from LogHelper import LogHelper

class TwoStringsAreClose:
    def __init__(self, word1: str, word2: str):
        LogHelper.PrintInput(word1)
        LogHelper.PrintInput(word2)
        LogHelper.PrintOutput(self.closeStrings(word1, word2))

    def getCharCount(self, my_string: str, chr: str) -> int:
        count = 0
        for char in my_string:
            if char == chr:
                count += 1
        return count

    def closeStrings(self, word1: str, word2: str) -> bool:

        set1 = set()
        set2 = set()
        dic1 = {}
        dic2 = {}

        for c in word1:
            set1.add(c)
        for c in word2:
            set2.add(c)

        if set1 != set2:
            return False

        for c in set1:
            dic1[c] = self.getCharCount(word1, c)
        for c in set2:
            dic2[c] = self.getCharCount(word2, c)

        print('start')
        print(dic1)
        print(dic2)

        for i, key1 in enumerate(dic1):
            for key2, value2 in islice(dic2.items(), i, None):
                if dic1[key1] == dic2[key2]:
                    tmp = dic2[key2]
                    dic2[key2] = dic2[key1]
                    dic2[key1] = tmp

        for i, key1 in enumerate(dic2):
            for key2, value2 in islice(dic1.items(), i, None):
                if dic2[key1] == dic1[key2]:
                    tmp = dic1[key2]
                    dic1[key2] = dic1[key1]
                    dic1[key1] = tmp

        print('end')
        print(dic1)
        print(dic2)

        return dic1 == dic2