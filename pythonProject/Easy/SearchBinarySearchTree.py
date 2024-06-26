from typing import Optional
from LogHelper import LogHelper
from TreeNode import TreeNode

class SearchBinarySearchTree:
    def __init__(self, root: Optional[TreeNode], val: int):
        LogHelper.PrintInput(root)
        LogHelper.PrintInput(val)
        LogHelper.PrintOutput(self.searchBST(root, val))

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is not None:
            if root.val == val:
                return root

            if root.left is not None:
                left = self.searchBST(root.left, val)
                if left is not None:
                    return left

            if root.right is not None:
                right = self.searchBST(root.right, val)
                if right is not None:
                    return right

        return None