# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)

        def dfs(node, pos, lvl):
            if not node:
                return
            
            levels[lvl].append(pos)
            
            dfs(node.left, 2 * pos, lvl + 1)
            dfs(node.right, 2 * pos + 1, lvl + 1)
            

        
        dfs(root, 0, 0)
        #print(levels)
        max_width = 0
        for key in levels:
            level = levels[key]
            max_width = max(max_width, level[-1] - level[0] + 1)
        
        return max_width

