# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = [0]
        def traversal(root):
            if not root:
                return
            if low <= root.val <= high:
                summ[0] += root.val
            traversal(root.right)
            traversal(root.left)

        traversal(root)
        return summ[0]
        