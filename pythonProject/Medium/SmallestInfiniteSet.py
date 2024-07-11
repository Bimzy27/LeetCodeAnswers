from queue import PriorityQueue

class SmallestInfiniteSet:
    infSet = PriorityQueue()
    def __init__(self):
        self.infSet = PriorityQueue()
        for i in range(int.ma):
            self.infSet.put(i + 1)
    def popSmallest(self) -> int:
        if len(self.infSet.queue) == 0:
            return 0
        smallest = self.infSet.get()
        print("smallest " + str(smallest))
        return smallest

    def addBack(self, num: int) -> None:
        if self.infSet.queue.__contains__(num):
            return
        self.infSet.put(num)
        print(len(self.infSet.queue))