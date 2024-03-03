# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        def merge(root1, root2, parent, signal):
            if not root1 and not root2:
                return
            elif root1 and not root2:
                node = TreeNode(root1.val)
                if signal == "left":
                    parent.left = node
                else:
                    parent.right = node
                merge(root1.left, root2, node, "left")
                merge(root1.right, root2, node, "right")
            
            elif not root1 and root2:
                node = TreeNode(root2.val)
                if signal == "left":
                    parent.left = node
                else:
                    parent.right = node
                merge(root1, root2.left, node, "left")
                merge(root1, root2.right, node, "right")

            elif root1 and root2:
                node = TreeNode()
                node.val = root1.val + root2.val
                if signal == "left":
                    parent.left = node
                else:
                    parent.right = node
                
                merge(root1.left, root2.left, node, "left")
                merge(root1.right, root2.right, node, "right")

        merge(root1, root2, dummy, "left")
        return dummy.left
                

        
            
        