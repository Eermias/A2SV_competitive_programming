# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        def preorder(root):
            if not root:
                return
            count[root.val] = 1 + count.get(root.val, 0)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        res = []
        for key, val in count.items():
            res.append([val, key])
        res.sort(reverse = True)
        maxx = res[0][0]
        ans = []
        for i in range(len(res)):
            if res[i][0] == maxx:
                ans.append(res[i][1])
            else:
                break

        return ans
        

        