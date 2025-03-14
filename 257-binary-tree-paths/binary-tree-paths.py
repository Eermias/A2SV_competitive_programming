# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        def findpath(node, path):
            if not node.left and not node.right:
                path.append(str(node.val))
                result.append('->'.join(path))
                path.pop()
                return
            
            path.append(str(node.val))
            if node.left:
                findpath(node.left, path)
            if node.right:
                findpath(node.right, path)
            path.pop()

        findpath(root, [])
        return result
            
