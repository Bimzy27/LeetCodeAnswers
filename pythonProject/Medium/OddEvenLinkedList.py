from typing import Optional, List

from ListNode import ListNode
from LogHelper import LogHelper


class OddEvenLinkedList:
    def __init__(self, head: Optional[ListNode]):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.oddEvenList(head))

    def GetListNodeFromList(self, nums: List[int]) -> Optional[ListNode]:
        head = None
        tail = None
        for num in nums:
            new_node = ListNode(num)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        odd = []

        index = 0
        while head is not None:
            if index % 2 == 0: # even
                even.append(head.val)
            else:
                odd.append(head.val)

            head = head.next
            index += 1

        return self.GetListNodeFromList(even + odd)
