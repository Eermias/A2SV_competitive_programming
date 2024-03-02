# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2: #both roots are null
                return True
            if not root1 or not root2: #only one of the two roots is null
                return False
            if root1.val != root2.val: #both roots are not null but have different values
                return False
            
            return(sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right))

        #ans = [False]
        if not root:
            return False
        if root.val == subRoot.val:
            if sameTree(root, subRoot):
                return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
            