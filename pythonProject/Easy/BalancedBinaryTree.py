from typing import Optional

from pythonProject.LogHelper import LogHelper
from pythonProject.TreeNode import TreeNode


class BalancedBinaryTree:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.isBalanced(root))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.balanced = True
        def dfs(node, depth) -> int:
            if not node:
                return depth

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)

            if abs(l - r) > 1:
                self.balanced = False

            return max(l, r)

        dfs(root, 0)

        return self.balanced
