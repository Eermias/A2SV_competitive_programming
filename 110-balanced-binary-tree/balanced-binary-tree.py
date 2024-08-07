# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0, True
            
            max_left, left = check(node.left)
            max_right, right = check(node.right)

            return 1 + max(max_left, max_right), abs(max_left - max_right) < 2 and left and right
        
        depth, result = check(root)
        return result
            