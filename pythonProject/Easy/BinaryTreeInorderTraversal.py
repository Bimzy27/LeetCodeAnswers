from typing import Optional, List

from LogHelper import LogHelper
from TreeNode import TreeNode


class BinaryTreeInorderTraversal:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.inorderTraversal(root))

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            lst: List[int] = []
            if node:
                lst += dfs(node.left)
                lst.append(node.val)
                lst += dfs(node.right)
            return lst

        return dfs(root)


