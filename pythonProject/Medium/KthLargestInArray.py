from queue import PriorityQueue
from typing import List

from pythonProject.LogHelper import LogHelper


class KthLargestInArray:
    def __init__(self, nums: List[int], k: int):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.findKthLargest(nums, k))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        prioQueue = PriorityQueue()
        for i, num in enumerate(nums):
            prioQueue.put((num * -1, num))
        for i in range(k - 1):
            prioQueue.get()
        return prioQueue.get()[1]