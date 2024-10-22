class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ans, min_reachable = -1, n + 1

        for city in range(n):
            distances = [float('inf') for _ in range(n)]
            distances[city] = 0

            for _ in range(n):
                relaxed = False
                for src, dest, weight in edges:
                    if distances[dest] > distances[src] + weight:
                        distances[dest] = distances[src] + weight
                        relaxed = True
                    if distances[src] > distances[dest] + weight:
                        distances[src] = distances[dest] + weight
                        relaxed = True

                if not relaxed:
                    break
            
            
            reachable = 0
            for distance in distances:
                if distance <= distanceThreshold:
                    reachable += 1
            
            if reachable <= min_reachable:
                ans = city
                min_reachable = reachable
        
        return ans