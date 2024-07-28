from typing import Optional, List

from LogHelper import LogHelper
from TreeNode import TreeNode


class BinaryTreePreorderTraversal:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.preorderTraversal(root))

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traverse(node):
            if not node:
                return
            output.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return output