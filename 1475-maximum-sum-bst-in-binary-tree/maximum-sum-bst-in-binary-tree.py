# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def max_BST(node):
            nonlocal max_sum
            if not node:
                return [True]
            if not node.left and not node.right:
                max_sum = max(max_sum, node.val)
                return [True, node.val, node.val, node.val]
            
            
            left = max_BST(node.left)
            right = max_BST(node.right)

            if len(left) == len(right) == 4:
                if (left[0] and right[0] and 
                    left[2] < node.val and right[1] > node.val):
                    curr_sum = left[3] + right[3] + node.val
                    max_sum = max(max_sum, curr_sum)
                    return [True, left[1], right[2], curr_sum]
                else:
                    return [False, 0, 0, max(left[3], right[3])]

            elif len(left) == 1:
                if right[0] and right[1] > node.val:
                    curr_sum = right[3] + node.val
                    max_sum = max(max_sum, curr_sum)
                    return [True, node.val, right[2], curr_sum]
                else:
                    return [False, 0, 0, right[3]]

            elif len(right) == 1:
                if left[0] and left[2] < node.val:
                    curr_sum = left[3] + node.val
                    max_sum = max(max_sum, curr_sum)
                    return [True, left[1], node.val, curr_sum]
                else:
                    return [False, 0, 0, left[3]]

        max_BST(root)
        return max_sum
            
            
            

