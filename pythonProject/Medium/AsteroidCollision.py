from typing import List

from LogHelper import LogHelper


class AsteroidCollision:
    def __init__(self, asteroids: List[int]):
        LogHelper.PrintInput(asteroids)
        LogHelper.PrintOutput(self.asteroidCollision(asteroids))

    def sameDir(self, left:int, right:int) -> bool:
        return left < 0 and right < 0 or left >= 0 and right >= 0

    def oppositeDir(self, left:int, right:int) -> bool:
        return left < 0 and right > 0

    def colliding(self, left:int, right:int) -> bool:
        return left > 0 and right < 0

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            num = asteroids[i]
            if len(stack) == 0:
                stack.append(num)
            elif self.sameDir(stack[-1], num):
                stack.append(num)
            elif self.oppositeDir(stack[-1], num):
                stack.append(num)
            elif self.colliding(stack[-1], num) and abs(stack[-1]) == abs(num):
                stack.pop()
            elif self.colliding(stack[-1], num) and abs(stack[-1]) < abs(num):
                stack.pop()
                i -= 1
            i += 1
        return stack
