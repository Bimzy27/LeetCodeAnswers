from LogHelper import LogHelper


class RemovingStarsFromString:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.removeStars(s))

    def remove_char_at_index(self, text: str, index: int) -> str:
        return text[:index] + text[index + 1:]

    def removeStars(self, s: str) -> str:
        index = 0
        while index < len(s):
            if s[index] == '*':
                if index == 0:
                    s = self.remove_char_at_index(s, 0)
                else:
                    s = self.remove_char_at_index(s, index - 1)
                    s = self.remove_char_at_index(s, index - 1)
                    index -= 1
            else:
                index += 1
        return s