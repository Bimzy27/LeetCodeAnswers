from LogHelper import LogHelper


class MaxNumVowelsInSubStrGivenLen:
    def __init__(self, s: str, k: int):
        LogHelper.PrintInput(s)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.maxVowels(s, k))

    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        max = 0

        iMin = 0
        iMax = 0

        st = ''

        while iMin < len(s):
            if iMax < len(s) and iMax - iMin <= k:
                st = s[iMax]
                if s[iMax] in vowels:
                    count += 1
                    if count >= k:
                        return k
                    if count > max:
                        max = count
                iMax += 1
            else:
                if count > 0 and s[iMin] in vowels:
                    count -= 1
                iMin += 1
        return max