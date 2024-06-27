from LogHelper import LogHelper
from TreeNode import TreeNode


class CountGoodNodesBinaryTree:
    def __init__(self, root: TreeNode):
        LogHelper.PrintInput(root)
        LogHelper.PrintOutput(self.goodNodes(root))

    def iterateGoodNodes(self, root: TreeNode, highest: int) -> int:
        count = 0
        if root.val > highest:
            highest = root.val

        if root.left is not None:
            if root.left.val >= highest:
                count += 1
            count += self.iterateGoodNodes(root.left, highest)

        if root.right is not None:
            if root.right.val >= highest:
                count += 1
            count += self.iterateGoodNodes(root.right, highest)

        return count

    def goodNodes(self, root: TreeNode) -> int:

        return self.iterateGoodNodes(root, root.val) + 1
