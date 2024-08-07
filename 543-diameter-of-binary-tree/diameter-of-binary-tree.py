# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_diameter(node):
            if not node:
                return 0, 0
            
            max_left, left = get_diameter(node.left)
            max_right, right = get_diameter(node.right)

            return 1 + max(max_left, max_right), max(left, right, max_left + max_right)
        
        depth, diameter = get_diameter(root)
        return diameter