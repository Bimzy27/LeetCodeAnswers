from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoSortedLists:
    def __init__(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        print(f"{list1} --- {list2} - Input")
        out = self.mergeTwoLists(list1, list2)
        print(f"{out} - Output")

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        listOut = None
        firstNode = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                localOut = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                localOut = ListNode(list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                localOut = ListNode(list1.val)
                list1 = list1.next
            else:
                localOut = ListNode(list2.val)
                list2 = list2.next

            if listOut is None:
                listOut = localOut
                firstNode = listOut
            else:
                listOut.next = localOut
                listOut = listOut.next

        return firstNode