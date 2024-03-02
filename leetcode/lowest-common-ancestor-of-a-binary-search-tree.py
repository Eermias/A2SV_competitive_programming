# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(parent, child):
            if not parent:
                return False
            if parent.val == child.val:
                return True
            if parent.val > child.val:
                return find(parent.left, child)
            if parent.val < child.val:
                return find(parent.right, child)
                
        if root.val == p.val and find(root, q) or root.val == q.val and find(root, p):
                return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val > p.val and root.val < q.val or root.val < p.val and root.val > q.val:
            return root

        
            

            

        