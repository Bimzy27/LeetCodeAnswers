class LargestSubstringNoRepeats:

    def __init__(self, s: str):
        self.lengthOfLongestSubstring(s)

    def lengthOfLongestSubstring(self, s: str) -> int:
        indexer = 0
        longestSubstring = 0
        while indexer <= len(s):
            mySet = set()
            for i in range(len(s) - indexer):
                index = i + indexer
                if s[index] in mySet:
                    break
                else:
                    mySet.add(s[index])

            if len(mySet) > longestSubstring:
                longestSubstring = len(mySet)
            indexer += 1
        return longestSubstring