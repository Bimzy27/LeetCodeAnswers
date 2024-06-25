from typing import List

from LogHelper import LogHelper


class DecodeString:
    def __init__(self, s: str):
        LogHelper.PrintInput(s)
        LogHelper.PrintOutput(self.decodeString(s))

    def decodeString(self, s: str) -> str:
        stack:[str] = []

        for char in s:
            if char == ']':
                substr = ''
                while stack[-1] != '[':
                    subchar = stack.pop()
                    substr = subchar + substr
                stack.pop()
                number = ''
                while len(stack) > 0 and stack[-1].isdigit():
                    number = stack.pop() + number
                for i in range(int(number)):
                    for c in substr:
                        stack.append(c)
            else:
                stack.append(char)

        print(stack)
        return ''.join(stack)