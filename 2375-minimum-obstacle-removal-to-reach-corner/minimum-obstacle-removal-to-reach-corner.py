class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        heap = [(0, 0, 0)] 
        processed = set()
        while heap:
            dist, row, col = heapq.heappop(heap)
            
            if (row, col) in processed:
                continue
            
            #print(row, col)
            if row == m - 1 and col == n - 1:
                return dist

            processed.add((row, col))
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_row = row + dr
                new_col = col + dc
                if -1 < new_row < m and -1 < new_col < n:
                    heapq.heappush(heap, (dist + grid[new_row][new_col], new_row, new_col))