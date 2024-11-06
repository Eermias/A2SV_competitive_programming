# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        summ = root.val
        root.val = -summ
        q = deque([root])
        while q:
            temp = 0
            for i in range(len(q)):
                node = q.popleft()
                node.val += summ
                curr = 0
                if node.right:
                    temp += node.right.val
                    curr += node.right.val
                    node.right.val = 0
                    q.append(node.right)
                if node.left:
                    temp += node.left.val
                    curr += node.left.val
                    node.left.val = 0
                    q.append(node.left)
                
                if node.right:
                    node.right.val -= curr
                if node.left:
                    node.left.val -= curr
            
            summ = temp
        
        return root
                
                
                

