from typing import Optional

from ListNode import ListNode
from LogHelper import LogHelper


class LinkedListCycle:
    def __init__(self, head):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.hasCycle(head))

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False