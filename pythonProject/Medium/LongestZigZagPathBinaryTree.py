from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class LongestZigZagPathBinaryTree:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.longestZigZag(root))

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node, prevDir: int, count: int):
            if not node:
                return

            self.max = max(count, self.max)

            if prevDir == -1:
                dfs(node.right, -1, 1)
                dfs(node.left, 1, count + 1)
            elif prevDir == 1:
                dfs(node.left, 1, 1)
                dfs(node.right, -1, count + 1)

        dfs(root, -1, 0)
        dfs(root, 1, 0)
        return self.max