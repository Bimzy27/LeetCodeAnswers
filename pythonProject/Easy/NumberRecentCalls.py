class RecentCounter:
    pQueue = []

    def __init__(self):
        pQueue = []

    def ping(self, t: int) -> int:
        self.pQueue.append(t)

        while self.pQueue[0] < t - 3000:
            self.pQueue.pop(0)

        print(len(self.pQueue))
        return len(self.pQueue)