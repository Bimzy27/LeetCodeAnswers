class LargestPalindromicSubstring:
    def __init__(self, s: str):
        self.longestPalindrome(s)

    def expand_around_center(self, s: str, left: int, right: int) -> str:
        """
        Expands around the center of the string to find the longest palindrome.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindrome in the given string using the expand around center approach.
        """
        if len(s) == 0:
            return ""

        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = self.expand_around_center(s, i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Check for even-length palindromes
            even_palindrome = self.expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
