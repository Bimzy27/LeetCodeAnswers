from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class PathSum:
    def __init__(self, root: Optional[TreeNode], targetSum: int):
        LogHelper.PrintInput(root)
        LogHelper.PrintInput(targetSum)
        LogHelper.PrintOutput(self.hasPathSum(root, targetSum))

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.hasPath = False
        def dfs(node, count):
            if not node:
                return
            count += node.val

            if not node.left and not node.right and count == targetSum:
                self.hasPath = True
            else:
                dfs(node.left, count)
                dfs(node.right, count)

        dfs(root, 0)
        return self.hasPath