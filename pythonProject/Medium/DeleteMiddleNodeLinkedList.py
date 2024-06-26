from typing import Optional, List
from ListNode import ListNode
from LogHelper import LogHelper


class DeleteMiddleNodeLinkedList:
    def __init__(self, head: Optional[ListNode]):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.deleteMiddle(head))

    def GetListNodeFromList(self, nums: List[int]) -> Optional[ListNode]:
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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head is not None:
            nodes.append(head.val)
            print("head: " + str(head.val))
            head = head.next

        nodes.pop(int(len(nodes) / 2))

        return self.GetListNodeFromList(nodes)