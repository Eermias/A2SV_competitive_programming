# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        def valid(root):
            if not root:
                return
            if not root.right and not root.left:
                return [root.val, root.val]
            right = valid(root.right)
            left = valid(root.left)
            if root.left and root.val < root.left.val or root.right and root.val > root.right.val:
                flag[0] = False
            if right and right[0] <= root.val or left and left[1] >= root.val:
                flag[0] = False
            minn = min(root.val, left[0]) if left else root.val
            maxx = max(root.val, right[1]) if right else root.val
            return [minn, maxx]

        valid(root)
        return flag[0]
            

             
            
            