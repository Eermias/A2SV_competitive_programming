# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(node):
            if not node:
                return None
            
            result = [node.val, node.val]
            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                ans[0] = max(ans[0], abs(node.val - left[0]), abs(node.val - left[1]))
                result[0] = min(result[0], left[0])
                result[1] = max(result[1], left[1])
            if right:
                ans[0] = max(ans[0], abs(node.val - right[0]), abs(node.val - right[1]))
                result[0] = min(result[0], right[0])
                result[1] = max(result[1], right[1])
            
            return result
        
        dfs(root)
        return ans[0]
