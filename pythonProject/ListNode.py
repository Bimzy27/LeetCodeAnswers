from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeHelper:
    @staticmethod
    def GetListNodeFromList(nums: List[int]) -> Optional[ListNode]:
        head = None  # Initialize head node as None
        tail = None  # Initialize tail node for efficient construction

        for num in nums:
            new_node = ListNode(num)  # Create a new ListNode for each element
            if head is None:  # If it's the first element
                head = new_node
                tail = new_node
            else:
                tail.next = new_node  # Link the current tail to the new node
                tail = new_node  # Update tail to point to the newly added node

        return head
