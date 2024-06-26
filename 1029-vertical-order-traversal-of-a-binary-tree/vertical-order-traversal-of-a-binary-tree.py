# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def dfs(node, col, level):
            if not node:
                return
            
            dfs(node.left, col - 1, level + 1)
            dfs(node.right, col + 1, level + 1)
            levels[col].append((level, node.val))
        
        dfs(root, 0, 0)
        keys = []
        for key in levels:
            keys.append(key)
        
        keys.sort()
        result = []
        for k in keys:
            level = levels[k]
            level.sort()
            temp = []
            for lvl, val in level:
                temp.append(val)
            result.append(temp)
        return result