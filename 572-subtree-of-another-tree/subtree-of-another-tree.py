# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
        
        q = deque()
        q.append([root, subRoot])
        while q:
            root1, root2 = q.popleft()
            if is_same(root1, root2):
                return True
            if root1:
                q.append([root1.left, root2])
                q.append([root1.right, root2])
        
        return False
    