# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf_nodes = []
        graph = defaultdict(list)
        def dfs(node):
            if not node.left and not node.right:
                leaf_nodes.append(node)
                return

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)
        
        dfs(root)

        def bfs(leaf):
            q = deque([[leaf, 0]])
            visited = {leaf}
            count = 0
            while q:
                node, dis = q.popleft()
                if dis and not node.left and not node.right:
                    count += 1
                elif dis < distance:
                    for child in graph[node]:
                        if child not in visited:
                            q.append([child, dis + 1])
                            visited.add(child)
            
            return count

        count = 0
        for leaf in leaf_nodes:
            count += bfs(leaf)
        
        return count // 2


        
        


        