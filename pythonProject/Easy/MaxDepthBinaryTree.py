from typing import Optional
from LogHelper import LogHelper
from TreeNode import TreeNode

class MaxDepthBinaryTree:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.maxDepth(root))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = 1
        right = 1

        if root.left != None:
            left = self.maxDepth(root.left) + 1
        if root.right != None:
            right = self.maxDepth(root.right) + 1

        if left > right:
            print("Root: " + str(root.val) + " Left: " + str(left))
            return left
        else:
            print("Root: " + str(root.val) + " Right: " + str(right))
            return right