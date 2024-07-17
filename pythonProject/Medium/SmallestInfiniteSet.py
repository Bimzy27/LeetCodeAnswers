from queue import PriorityQueue

class SmallestInfiniteSet:
    def __init__(self):
        nums = list(range(1, 1001))
        self.sNums = set(nums)
    def popSmallest(self) -> int:
        small = min(self.sNums)
        self.sNums.remove(small)
        return small

    def addBack(self, num: int) -> None:
        self.sNums.add(num)