# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower, upper):
            if not node:
                return True
            
            if lower >= node.val or upper <= node.val:
                return False
            left = validate(node.left, lower, min(upper, node.val))
            right = validate(node.right, max(lower, node.val), upper)

            return left and right

        return validate(root, float("-inf"), float("inf"))
        
            

             
            
            