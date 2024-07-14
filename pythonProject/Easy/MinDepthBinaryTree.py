from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class MinDepthBinaryTree:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.minDepth(root))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.minD = -1

        if not root:
            return 0

        def dfs(node:TreeNode, depth: int):
            if not node.left and not node.right:
                if self.minD == -1:
                    self.minD = depth
                else:
                    self.minD = min(self.minD, depth)
            depth += 1
            if node.left:
                dfs(node.left, depth)
            if node.right:
                dfs(node.right, depth)

        dfs(root, 1)
        return self.minD