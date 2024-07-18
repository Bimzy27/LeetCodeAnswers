from typing import List

from LogHelper import LogHelper


class LetterCombinationsPhoneNumber:
    def __init__(self, digits: str):
        LogHelper.PrintInput(digits)
        LogHelper.PrintOutput(self.letterCombinations(digits))

    def letterCombinations(self, digits: str) -> List[str]:
        numToLets = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        out = []
        dLen = len(digits)
        def backtrack(i, string):
            if len(string) == dLen:
                out.append(string)
                return

            for c in numToLets[int(digits[i])]:
                backtrack(i + 1, string + c)

        if digits:
            backtrack(0, "")

        return out
