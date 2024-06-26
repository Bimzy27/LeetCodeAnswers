from typing import Optional, List
from ListNode import ListNode
from LogHelper import LogHelper


class DeleteMiddleNodeLinkedList:
    def __init__(self, head: Optional[ListNode]):
        LogHelper.PrintInput(head)
        LogHelper.PrintOutput(self.deleteMiddle(head))

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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head is not None:
            nodes.append(head.val)
            print("head: " + str(head.val))
            head = head.next

        nodes.pop(int(len(nodes) / 2))

        return self.GetListNodeFromList(nodes)