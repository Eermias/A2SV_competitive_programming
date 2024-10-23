class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.shortest = [[float('inf')] * n for _ in range(n)]
        self.n = n

        for i in range(n):
            self.shortest[i][i] = 0
        
        for u, v, weight in edges:
            self.shortest[u][v] = weight
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.shortest[i][j] > self.shortest[i][k] + self.shortest[k][j]:
                        self.shortest[i][j] = self.shortest[i][k] + self.shortest[k][j]
        

    def relax(self, u, v):
            for i in range(self.n):
                for j in range(self.n):
                    prev = self.shortest[i][u]
                    after = self.shortest[v][j]
                    if self.shortest[i][j] > prev + self.shortest[u][v] + after:
                        self.shortest[i][j] = prev + self.shortest[u][v] + after
        

    def addEdge(self, edge: List[int]) -> None:
        u, v, weight = edge
        if self.shortest[u][v] > weight:
            self.shortest[u][v] = weight
            self.relax(u, v)

    def shortestPath(self, node1: int, node2: int) -> int:

        res = self.shortest[node1][node2]
        return res if res != float('inf') else -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)