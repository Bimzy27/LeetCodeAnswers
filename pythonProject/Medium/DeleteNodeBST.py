from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class DeleteNodeBST:
    def __init__(self, root: Optional[TreeNode], key: int):
        LogHelper.PrintInput(root)
        LogHelper.PrintInput(key)
        LogHelper.PrintOutput(self.deleteNode(root, key))

    def smallestChild(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                tmp = self.smallestChild(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)

        return root
