# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [-1]
        def find(node):
            nonlocal k
            if not node:
                return
            
            find(node.left)
            k -= 1
            if k == 0:
                result[0] = node.val
            find(node.right)
        
        find(root)
        return result[0]


            
