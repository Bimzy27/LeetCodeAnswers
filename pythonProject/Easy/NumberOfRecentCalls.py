from typing import List


class NumberOfRecentCalls:
    queue: List[int] = []
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        offset = t - 3000
        while len(self.queue) > 0 and self.queue[0] < offset:
            self.queue.pop(0)

        self.queue.append(t)
        return len(self.queue)
