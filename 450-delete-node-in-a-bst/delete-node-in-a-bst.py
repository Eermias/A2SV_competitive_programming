# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            while node.left:
                node = node.left
            return node
        
        def search(node):
            if not node:
                return None

            if node.val == key:
                if node.left and node.right:
                    successor = find_min(node.right)
                    node.val = successor.val
                    successor.val = key
                    node.right = search(node.right)
                    return node

                elif node.left:
                    return node.left

                return node.right
                
                
                

            elif node.val > key:
                node.left = search(node.left)
            else:
                node.right = search(node.right)
            
            return node
        
        return search(root)
            

            


            