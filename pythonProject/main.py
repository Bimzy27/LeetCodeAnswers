from Easy.LeafSimilarTree import LeafSimilarTree
from TreeNode import TreeNodeHelper

if __name__ == '__main__':
    main = LeafSimilarTree(
        TreeNodeHelper.GetTreeNodeFromList([3,5,1,6,2,9,8,None,None,7,4]),
        TreeNodeHelper.GetTreeNodeFromList([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    )
