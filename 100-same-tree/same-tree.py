# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque()
        que.append([p, q])
        while que:
            node1, node2 = que.popleft()
            if node1 == node2 == None:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            que.append([node1.left, node2.left])
            que.append([node1.right, node2.right])
        
        return True
            