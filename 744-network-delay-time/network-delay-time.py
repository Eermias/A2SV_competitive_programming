class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
    
        time_needed = {node : float("inf") for node in range(1, n + 1)}
        time_needed[k] = 0

        heap = [[0, k]]
        processed = set()
        while heap:
            cost, node = heapq.heappop(heap)
            if node in processed:
                continue
            
            for child, weight in graph[node]:
                if time_needed[child] > cost + weight:
                    time_needed[child] = cost + weight
                    heapq.heappush(heap, [time_needed[child], child])

            processed.add(node)


        shortest = max(time_needed.values())
        if shortest == float("inf"):
            return -1
        return shortest