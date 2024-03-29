# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
            return #NO NEED in PYTHON just a good practice
        inorder(root)
        return ans
        