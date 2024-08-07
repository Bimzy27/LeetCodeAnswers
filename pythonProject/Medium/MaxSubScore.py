import heapq
from queue import PriorityQueue
from typing import List

from LogHelper import LogHelper


class MaxSubScore:
    def __init__(self, nums1: List[int], nums2: List[int], k: int):
        LogHelper.PrintInput(nums1)
        LogHelper.PrintInput(nums2)
        LogHelper.PrintInput(k)
        LogHelper.PrintOutput(self.maxScore(nums1, nums2, k))

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        minHeap = []
        n1Sum = 0
        result = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
            if len(minHeap) == k:
                result = max(result, n1Sum * n2)
        return result