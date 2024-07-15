from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class SameTree:
    def __init__(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        LogHelper.PrintInput(p)
        LogHelper.PrintInput(q)
        LogHelper.PrintOutput(self.isSameTree(p, q))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True

        def dfs(node1, node2):
            if not self.isSame:
                return

            if not node1 and not node2:
                return

            if not node1 or not node2:
                self.isSame = False
                return

            if node1.val != node2.val:
                self.isSame = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p, q)

        return self.isSame
