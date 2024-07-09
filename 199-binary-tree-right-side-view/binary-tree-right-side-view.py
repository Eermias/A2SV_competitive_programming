# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        q.append(root)

        while q:
            right_most = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right_most = node.val
                    q.append(node.left)
                    q.append(node.right)
            
            if right_most != None:
                result.append(right_most)
        
        return result

            
        