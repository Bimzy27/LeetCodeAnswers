from typing import List

from LogHelper import LogHelper


class UniqueOccurrences:
    def __init__(self, arr: List[int]):
        LogHelper.PrintInput(arr)
        LogHelper.PrintOutput(self.uniqueOccurrences(arr))

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sorted = {}

        for i, num in enumerate(arr):
            count = sorted.get(num, 0)
            sorted[num] = count + 1

        unique = set()

        for num in sorted.values():
            if unique.__contains__(num):
                return False

            unique.add(num)
        return True