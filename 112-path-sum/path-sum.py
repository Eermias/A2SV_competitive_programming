# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def path_sum(node, curr_sum):
            if not node.left and not node.right:
                if curr_sum + node.val == targetSum:
                    return True
                return False
            
            left, right = False, False
            if node.left:
                left = path_sum(node.left, curr_sum + node.val)
            if node.right:
                right = path_sum(node.right, curr_sum + node.val)

            return left or right
        
        if not root:
            return False
        return path_sum(root, 0)
            
