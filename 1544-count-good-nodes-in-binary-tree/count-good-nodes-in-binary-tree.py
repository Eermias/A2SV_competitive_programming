# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque([[root, float("-inf")]])
        while q:
            node, maxx = q.popleft()
            if node and node.val >= maxx:
                count += 1
            if node:
                maxx = max(maxx, node.val)
                q.append([node.left, maxx])
                q.append([node.right, maxx])
        
        return count
