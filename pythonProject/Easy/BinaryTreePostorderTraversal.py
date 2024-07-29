from typing import Optional, List

from LogHelper import LogHelper
from TreeNode import TreeNode


class BinaryTreePostorderTraversal:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.postorderTraversal(root))

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traverse(node):
            if not node:
                return



        traverse(root)
        return output