class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            count = 1
            for child in graph[node]:
                count += dfs(child)
            
            return count
        
        visited = set()
        unreachable_pairs = 0
        for i in range(n):
            connected = dfs(i)
            print(i, connected)
            unreachable_pairs += (n - connected) * connected
        
        return unreachable_pairs // 2

