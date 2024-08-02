from typing import List


class MajorityElement:

    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()

        for n in nums:
            if not counts.__contains__(n):
                counts[n] = 0
            counts[n] += 1

        return max(counts, key=counts.get)