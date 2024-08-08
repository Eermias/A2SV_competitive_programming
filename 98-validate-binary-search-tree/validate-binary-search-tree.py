# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([root, float("-inf"), float("inf")])
        while q:
            node, minn, maxx = q.popleft()
            if node and not minn < node.val < maxx:
                return False
            if node:
                q.append([node.left, minn, min(maxx, node.val)])
                q.append([node.right, max(minn, node.val), maxx])
        
        return True