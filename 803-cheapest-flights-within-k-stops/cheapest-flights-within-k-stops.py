class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append([end, price])

        dp = [[float('inf')] * n for _ in range(n + 1)]
        dp[0][src] = 0

        for steps in range(1, n + 1):
            dp[steps][src] = 0
            for node in range(n):
                for city, price in graph[node]:
                    dp[steps][city] = min(dp[steps][city], dp[steps - 1][city], dp[steps - 1][node] + price)

        res = dp[k + 1][dst]
        return res if res != float('inf') else -1
