# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([root, 0])
        max_width = 0
        while q:
            level = []
            for _ in range(len(q)):
                node, idx = q.popleft()
                level.append(idx)
                if node.left:
                    q.append([node.left, idx * 2])
                if node.right:
                    q.append([node.right, idx * 2 + 1])
            max_width = max(max_width, level[-1] - level[0] + 1)
        
        return max_width

