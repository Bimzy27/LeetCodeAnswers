from typing import Optional

from ListNode import ListNode
from LogHelper import LogHelper


class RemoveDuplicatesSortedList:
    def __init__(self, head: Optional[ListNode]):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.deleteDuplicates(head))

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = head
        while next != None:
            if next.next and next.next.val == next.val:
                next.next = next.next.next
                continue
            next = next.next

        next = head
        while next != None:
            print(next.val)
            next = next.next

        return head