from typing import Optional

from LogHelper import LogHelper

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class ReverseLinkedList:
    def __init__(self, head: Optional[ListNode]):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.reverseList(head))

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_node = curr.next  # Store the next node before overwriting
            curr.next = prev  # Reverse the link
            prev = curr  # Move pointers
            curr = next_node  # Move to the next node

        return prev