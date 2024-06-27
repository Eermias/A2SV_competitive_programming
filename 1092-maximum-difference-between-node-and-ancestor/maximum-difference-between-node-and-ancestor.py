class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        q = deque()
        q.append([root, root.val, root.val])

        while q:
            node, minn, maxx = q.popleft()
            curr = node.val
            max_diff = max(max_diff, curr - minn, maxx - curr)

            if node.left:
                q.append([node.left, min(minn, node.left.val), max(maxx, node.left.val)])
            if node.right:
                q.append([node.right, min(minn, node.right.val), max(maxx, node.right.val)])
        
        return max_diff