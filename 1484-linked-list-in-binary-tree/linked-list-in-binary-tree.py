# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check(root, head):
            if not head:
                return True
            if not root:
                return False
            if head.val != root.val:
                return False
            
            left = check(root.left, head.next)
            right = check(root.right, head.next)

            return right or left
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == head.val:
                if check(node, head):
                    return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False