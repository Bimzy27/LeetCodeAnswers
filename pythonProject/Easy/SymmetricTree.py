from collections import defaultdict
from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class SymmetricTree:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.isSymmetric(root))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftSide = defaultdict(str)
        rightSide = defaultdict(str)

        def dfs(isLeft, node, depth):
            if not node:
                if isLeft:
                    leftSide[depth] += "-"
                else:
                    rightSide[depth] = "-" + rightSide[depth]
                return
            if isLeft:
                leftSide[depth] += str(node.val)
            else:
                rightSide[depth] = str(node.val) + rightSide[depth]

            dfs(isLeft, node.left, depth + 1)
            dfs(isLeft, node.right, depth + 1)

        if root.left:
            dfs(True, root.left, 0)
        if root.right:
            dfs(False, root.right, 0)

        return leftSide == rightSide