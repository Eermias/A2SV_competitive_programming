class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            for ngbr in adj_list[node]:
                if ngbr not in visited:
                    if dfs(ngbr):
                        return True
            
            return False

        return dfs(source)