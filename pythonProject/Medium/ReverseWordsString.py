from LogHelper import LogHelper


class ReverseWordsString:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.reverseWords(s))

    def reverseWords(self, s: str) -> str:
        if len(s) <= 1:
            return s

        sList = list(s)
        wordList: list[str] = []
        iteratingWord = False
        word: str = ""
        for i in range(len(sList)):
            if iteratingWord == False and sList[i] != ' ':
                iteratingWord = True
                word = sList[i]
            elif iteratingWord == False:
                continue
            elif iteratingWord == True and sList[i] != ' ':
                word += sList[i]
            else:
                wordList.append(word)
                iteratingWord = False

        if iteratingWord == True:
            wordList.append(word)

        output: str = ""
        wordList.reverse()
        for i in range(len(wordList)):
            output += wordList[i]
            output += ' '
        output = output[:-1]
        return output
