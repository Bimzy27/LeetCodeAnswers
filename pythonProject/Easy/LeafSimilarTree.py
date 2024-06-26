from typing import Optional, List

from LogHelper import LogHelper
from TreeNode import TreeNode


class LeafSimilarTree:
    def __init__(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        LogHelper.PrintInput(root1)
        LogHelper.PrintInput(root2)
        LogHelper.PrintOutput(self.leafSimilar(root1, root2))



    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        nodes1:List[int] = []
        nodes2:List[int] = []

        self.tryAddNode(root1, nodes1)
        self.tryAddNode(root2, nodes2)

        print(nodes1)
        print(nodes2)

        return nodes1 == nodes2

    def tryAddNode(self, root: Optional[TreeNode], nodes: List[int]):
        if root.left is None and root.right is None:
            nodes.append(root.val)
            return

        if root.left is not None:
            self.tryAddNode(root.left, nodes)
        if root.right is not None:
            self.tryAddNode(root.right, nodes)