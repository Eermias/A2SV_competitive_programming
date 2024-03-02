# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = [0]
        def diameter(treeRoot):
            if not treeRoot:
                return 0
            right = diameter(treeRoot.right)
            left = diameter(treeRoot.left)
            maxLen[0] = max(maxLen[0], right + left)
            return 1 + max(right, left)

        diameter(root)
        return maxLen[0]
        