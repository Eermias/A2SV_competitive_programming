class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append((v, w))
       
    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float('inf')] * self.n
        distances[node1] = 0
        heap = [(0, node1)]
        processed = set()
        while heap:
            cost, node = heapq.heappop(heap)

            if node in processed:
                continue
            if node == node2:
                return cost
            
            processed.add(node)
            for child, weight in self.graph[node]:
                if weight + cost < distances[child]:
                    heapq.heappush(heap, (weight + cost, child))
                    distances[child] = weight + cost
           
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)