import heapq
from typing import List

from LogHelper import LogHelper


class TotalCostKWorkers:
    def __init__(self, costs: List[int], k: int, candidates: int):
        LogHelper.PrintInput(costs)
        LogHelper.PrintInput(k)
        LogHelper.PrintInput(candidates)
        LogHelper.PrintOutput(self.totalCost(costs, k, candidates))

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l, r = 0, len(costs) - 1
        total = 0
        lHeap, rHeap = [], []
        maxi = max(costs)

        for i in range(k):
            while len(lHeap) < candidates and l <= r:
                heapq.heappush(lHeap, costs[l])
                l += 1

            while len(rHeap) < candidates and l <= r:
                heapq.heappush(rHeap, costs[r])
                r -= 1

            if len(lHeap) == 0:
                heapq.heappush(lHeap, maxi)
            elif len(rHeap) == 0:
                heapq.heappush(rHeap, maxi)

            increment = heapq.heappop(lHeap) if lHeap[0] <= rHeap[0] else heapq.heappop(rHeap)
            total += increment

        return total