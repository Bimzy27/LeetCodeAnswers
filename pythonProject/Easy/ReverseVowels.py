from LogHelper import LogHelper


class ReverseVowels:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.reverseVowels(s))

    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sList = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if sList[left] in vowels and sList[right] in vowels:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
            elif sList[left] in vowels:
                right -= 1
            elif sList[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1

        return ''.join(sList)
