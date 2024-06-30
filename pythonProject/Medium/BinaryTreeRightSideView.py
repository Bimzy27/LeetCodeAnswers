from typing import Optional, List

from LogHelper import LogHelper
from TreeNode import TreeNode


class BinaryTreeRightSideView:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.rightSideView(root))

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dic = dict()

        def bfs(node:Optional[TreeNode], depth):

            if node is not None:

                if not dic.__contains__(depth):
                    dic[depth] = node.val

                bfs(node.right, depth + 1)
                bfs(node.left, depth + 1)

        bfs(root, 0)

        return [value for value in dic.values() if isinstance(value, int)]
