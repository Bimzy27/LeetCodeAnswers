from typing import List, Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class ConvertSortedArrayToBinarySearchTree:
    def __init__(self, nums: List[int]):
        LogHelper.PrintInput(nums)
        LogHelper.PrintOutput(self.sortedArrayToBST(nums))

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nLen = len(nums)

        if nLen == 0:
            return None

        mid = nLen // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

