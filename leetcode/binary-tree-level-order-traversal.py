# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        levels = maxDepth(root)
        res = [[] for _ in range(levels)]
        print(res)
        def preorder(root, level):
            if not root:
                return
            res[level].append(root.val)
            preorder(root.left, level + 1)
            preorder(root.right, level + 1)

        preorder(root, 0)
        return res


        