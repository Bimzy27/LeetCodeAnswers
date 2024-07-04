from LogHelper import LogHelper


class IndexFirstOccurenceInString:
    def __init__(self, haystack: str, needle: str):
        LogHelper.PrintInput(haystack)
        LogHelper.PrintInput(needle)
        LogHelper.PrintOutput(self.strStr(haystack, needle))

    def strStr(self, haystack: str, needle: str) -> int:
        counter = 0
        needleLen = len(needle)

        while len(haystack) > 0:
            if haystack[0] == needle[0]:
                if haystack[:needleLen] == needle:
                    return counter
            counter += 1
            haystack = haystack[1::]
        return -1
