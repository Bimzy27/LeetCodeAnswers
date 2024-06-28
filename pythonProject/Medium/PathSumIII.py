from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class PathSumIII:
    def __init__(self, root: Optional[TreeNode], targetSum: int):
        LogHelper.PrintInput(root)
        LogHelper.PrintInput(targetSum)
        LogHelper.PrintOutput(self.pathSum(root, targetSum))

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0

        def traverse(node, cur):
            if not node:
                return
            traverse(node.left, cur + node.val)
            traverse(node.right, cur + node.val)
            if cur + node.val == targetSum:
                self.total += 1

        def dfs(node):
            if not node:
                return
            traverse(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.total