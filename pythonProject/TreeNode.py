import collections
from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class TreeNodeHelper:
    @staticmethod
    def GetTreeNodeFromList(nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root = TreeNode(nums[0])  # Root node from the first element
        queue = collections.deque([root])  # Queue for level-order processing

        i = 1
        while queue and i < len(nums):
            current_node = queue.popleft()
            # Check if there are elements left for left and right children
            if i < len(nums):
                left_child = TreeNode(nums[i]) if nums[i] else None
                current_node.left = left_child
                queue.append(left_child)
                i += 1
            if i < len(nums):
                right_child = TreeNode(nums[i]) if nums[i] else None
                current_node.right = right_child
                queue.append(right_child)
                i += 1

        return root