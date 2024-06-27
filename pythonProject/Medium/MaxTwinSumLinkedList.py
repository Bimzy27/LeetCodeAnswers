from typing import Optional

from ListNode import ListNode
from LogHelper import LogHelper


class MaxTwinSumLinkedList:
    def __init__(self, head: Optional[ListNode]):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.pairSum(head))

    def pairSum(self, head: Optional[ListNode]) -> int:

        nxt = head
        n = 0

        while nxt.next is not None:
            nxt = nxt.next
            n += 1

        vals = dict()
        half = int(n / 2)
        forward = True
        index = 0

        while head is not None:
            if vals.__contains__(index):
                vals[index] += head.val
            else:
                vals[index] = head.val

            if forward and index >= half:
                forward = False
            elif forward:
                index += 1
            else:
                index -= 1

            head = head.next

        return sorted(vals.values())[-1]