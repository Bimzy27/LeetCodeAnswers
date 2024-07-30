from typing import Optional

from ListNode import ListNode
from LogHelper import LogHelper


class IntersectionTwoLinkedLists:
    def __init__(self, headA: ListNode, headB: ListNode):
        LogHelper.PrintInput(headA)
        LogHelper.PrintInput(headB)
        LogHelper.PrintOutput(self.getIntersectionNode(headA, headB))

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        node = headA

        while node:
            setA.add(node)
            node = node.next

        node = headB
        while node:
            if node in setA:
                return node
            node = node.next

        return None