# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []

            combo = []
            for ans in dfs(node.left):
                combo.append(str(node.val) + ans)
            for ans in dfs(node.right):
                combo.append(str(node.val) + ans)
            
            return combo if combo else [str(node.val)]
        
        result = dfs(root)
        print(result)
        total = 0
        for num in result:
            total += int(num)
        return total 
        
