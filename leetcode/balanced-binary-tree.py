# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = [True]
        def maxDepth(root):
            if not root:
                return 0
            rightHeight = maxDepth(root.right)
            leftHeight = maxDepth(root.left)
            if abs(rightHeight - leftHeight) > 1:
                ans[0] = False
            return 1 + max(rightHeight, leftHeight)
        
        maxDepth(root)
        return ans[0]
        
        

