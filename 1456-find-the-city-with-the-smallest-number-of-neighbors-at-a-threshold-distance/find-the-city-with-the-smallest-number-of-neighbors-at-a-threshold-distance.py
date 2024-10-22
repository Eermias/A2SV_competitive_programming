class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # initialize distance matrix
        distance = [[float('inf')] * n for _ in range(n)]

        # initialize distance from each node to itself to 0
        for i in range(n):
            distance[i][i] = 0

        # populate the initial give edges
        for u, v, w in edges:
            distance[u][v] = distance[v][u] = w

        # apply Floyd - Warshall's algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        # count the number of reachable cities from each city within the distanceThreshold
        reachable = [0] * n
        for i in range(n):
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    reachable[i] += 1

        # find the largest numbered city with the lowest number of reachble cities 
        min_reachable = float('inf')
        desired_city = -1
        for city in range(n):
            if reachable[city] <= min_reachable:
                min_reachable = reachable[city]
                desired_city = city
        
        return desired_city