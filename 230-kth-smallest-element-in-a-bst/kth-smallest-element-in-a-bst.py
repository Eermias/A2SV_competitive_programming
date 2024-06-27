# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [0, 0] #[ans, count]
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            result[1] += 1
            if result[1] == k:
                result[0] = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return result[0]

        