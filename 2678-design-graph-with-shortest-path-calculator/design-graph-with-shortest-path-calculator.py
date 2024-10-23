class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = {i: [] for i in range(n)}
        for u, v, weight in edges:
            self.graph[u].append((v, weight))

    def addEdge(self, edge: List[int]) -> None:
        u, v, weight = edge
        self.graph[u].append((v, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        cost = [inf] * len(self.graph)

        while pq:
            weight, node = heapq.heappop(pq)
            if weight > cost[node]:
                continue
            if node == node2:
                return weight
            for nbr, w in self.graph[node]:
                new_cost = weight + w
                if new_cost < cost[nbr]:
                    cost[nbr] = new_cost
                    heappush(pq, (new_cost, nbr))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)