class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            q = deque([(r, c)])
            visited = {(r, c)}
            perimeter = 0
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if -1 < nr < len(grid) and -1 < nc < len(grid[0]) and grid[nr][nc] == 1:
                        if (nr, nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))
                    else:
                        perimeter += 1
            
            return perimeter
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return bfs(r, c)