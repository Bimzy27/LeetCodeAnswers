from queue import PriorityQueue

class SmallestInfiniteSet:
    infSet = PriorityQueue()
    def __init__(self):
        print("constructed")
    def popSmallest(self) -> int:
        return self.infSet.pop(0)

    def addBack(self, num: int) -> None:
        self.infSet.add(num)