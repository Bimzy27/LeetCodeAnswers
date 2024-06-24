from ListNode import ListNodeHelper
from Medium.AddTwoNumbers import AddTwoNumbers

if __name__ == '__main__':
    node1 = ListNodeHelper.GetListNodeFromList([2, 4, 3])
    node2 = ListNodeHelper.GetListNodeFromList([5, 6, 4])
    main = AddTwoNumbers(node1, node2)
