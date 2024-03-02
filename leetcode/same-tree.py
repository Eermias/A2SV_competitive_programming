# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = [True]
        def same(root1, root2):
            if not root1 and not root2:
                return
            elif (root1 and not root2) or (root2 and not root1):
                ans[0] = False
                return
            elif root1 and root2 and root1.val != root2.val:
                ans[0] = False
                return
            same(root1.left, root2.left)
            same(root1.right, root2.right)
            return
        
        same(p, q)
        return ans[0]
        