# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_path(node, path, val):
            if not node:
                return []
            if node.val == val:
                return path
            
            path.append('L')
            if get_path(node.left, path, val):
                return path
            path.pop()
            path.append('R')
            if get_path(node.right, path, val):
                return path
            path.pop()
            return []
        
        start = get_path(root, [], startValue)
        dest = get_path(root, [], destValue)

        n = min(len(start), len(dest))
        i = 0
        while i < n:
            if start[i] != dest[i]:
                break
            i += 1
            
        start = start[i:]
        dest = dest[i:]
        start = ['U'] * len(start)
        return "".join(start) + "".join(dest)
            
            
