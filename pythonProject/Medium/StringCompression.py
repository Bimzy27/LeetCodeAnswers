from typing import List

from LogHelper import LogHelper


class StringCompression:
    def __init__(self, chars: List[str]):
        LogHelper.PrintInput(chars)
        LogHelper.PrintOutput(self.compress(chars))

    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        charsNew: List[str] = []
        curChar = ''
        counter = 0
        for char in chars:
            if char == curChar:
                counter += 1
            else:
                if curChar != '':
                    charsNew.append(curChar)
                    if counter > 1:
                        if counter > 9:
                            numStr = str(counter)
                            for digitChar in numStr:
                                charsNew.append(f"{digitChar}")
                        else:
                            charsNew.append(f"{counter}")
                curChar = char
                counter = 1

        if curChar != '':
            charsNew.append(curChar)
            if counter > 1:
                if counter > 9:
                    numStr = str(counter)
                    for digitChar in numStr:
                        charsNew.append(f"{digitChar}")
                else:
                    charsNew.append(f"{counter}")

        chars.clear()
        for char in charsNew:
            chars.append(char)
        print(chars)
        return len(chars)