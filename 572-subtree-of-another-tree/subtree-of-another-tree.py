# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False

            left = check(root1.left, root2.left)
            right = check(root1.right, root2.right)

            return left and right
        
        def traverse(node):
            if not node:
                return False
            
            if node.val == subRoot.val and check(node, subRoot):
                return True
            
            left = traverse(node.left)
            right = traverse(node.right)

            return left or right
        
        return traverse(root)

            
            