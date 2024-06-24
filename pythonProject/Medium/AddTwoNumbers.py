from typing import Optional
from ListNode import ListNode
from LogHelper import LogHelper

class AddTwoNumbers:
    def __init__(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        LogHelper.PrintInput(l1)
        LogHelper.PrintInput(l2)
        LogHelper.PrintOutput(self.addTwoNumbers(l1, l2))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        exponent = 1
        num1 = 0
        while l1 is not None:
            num1 += l1.val * exponent
            exponent *= 10
            l1 = l1.next

        exponent = 1
        num2 = 0
        while l2 is not None:
            num2 += l2.val * exponent
            exponent *= 10
            l2 = l2.next

        num3 = num1 + num2
        num_str = str(num3)
        node:Optional[ListNode] = None
        for digit in num_str:
            node = ListNode(int(digit), node)
            print(digit)  # Process or print the digit
        return node