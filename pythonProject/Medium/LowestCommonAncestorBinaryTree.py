from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class LowestCommonAncestorBinaryTree:
    def __init__(self, root: TreeNode, p: TreeNode, q: TreeNode):
        LogHelper.PrintInput(root)
        LogHelper.PrintInput(p)
        LogHelper.PrintInput(q)
        LogHelper.PrintOutput(self.lowestCommonAncestor(root, p, q))

    def lowestCommonAncestor(self, root: TreeNode, p, q) -> int:
        self.lowest: Optional[TreeNode] = None
        self.lowDepth = 0

        def dfs(node, depth: int):
            if not node:
                return
            print("Val: " + str(node.val) + " depth: " + str(depth))

            hasP = False
            hasQ = False

            if node.val == p:
                hasP = True

            if node.val == q:
                hasQ = True

            if node.left:
                lP, lQ = dfs(node.left, depth + 1)
                if lP:
                    hasP = True
                if lQ:
                    hasQ = True
            if node.right:
                rP, rQ = dfs(node.right, depth + 1)
                if rP:
                    hasP = True
                if rQ:
                    hasQ = True

            if hasP and hasQ and depth > self.lowDepth:
                self.lowDepth = depth
                self.lowest = node
                print("Set lowest " + str(node.val))

            return hasP, hasQ

        dfs(root, 1)

        if self.lowest is None:
            return -1
        return self.lowest.val
