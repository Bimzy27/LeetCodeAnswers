from typing import Optional

from LogHelper import LogHelper
from TreeNode import TreeNode


class MaximumLevelSumBinaryTree:
    def __init__(self, root: Optional[TreeNode]):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.maxLevelSum(root))

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dic = dict()

        def bfs(node: Optional[TreeNode], depth):

            if node is not None:

                if dic.__contains__(depth):
                    dic[depth] += node.val
                else:
                    dic[depth] = node.val

                bfs(node.right, depth + 1)
                bfs(node.left, depth + 1)

        bfs(root, 1)

        max_value = max(dic.values())
        max_key = [key for key, value in dic.items() if value == max_value][0]

        return max_key