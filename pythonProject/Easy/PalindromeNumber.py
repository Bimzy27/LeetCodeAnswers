from LogHelper import LogHelper


class PalindromeNumber:
    def __init__(self, x: int):
        LogHelper.PrintInput(x)
        LogHelper.PrintOutput(self.isPalindrome(x))

    def isPalindrome(self, x: int) -> bool:
        digits = [int(digit) for digit in str(x)]
        return digits == digits[::-1]