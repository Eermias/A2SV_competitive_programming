# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def isGood(root, maxx):
            if not root:
                return
            if root.val >= maxx:
                count[0] += 1
            maxx = max(maxx, root.val)
            isGood(root.left, maxx)
            isGood(root.right, maxx)

        isGood(root, root.val)
        return count[0]
        