class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        res = 1
        bounds = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 1:
                    continue
                curr_size = 1
                grid[i][j] = -1
                queue = collections.deque([(i,j)])
                curr_bounds = set()
                while queue:
                    r,c = queue.popleft()
                    if r-1 >= 0:
                        if grid[r-1][c] == 0:
                            curr_bounds.add((r-1,c))
                        elif grid[r-1][c] == 1:
                            curr_size += 1
                            grid[r-1][c] = -1
                            queue.append((r-1, c))
                    if c-1 >= 0:
                        if grid[r][c-1] == 0:
                            curr_bounds.add((r, c-1))
                        elif grid[r][c-1] == 1:
                            curr_size+= 1
                            grid[r][c-1] = -1
                            queue.append((r, c-1))
                    if r+1<len(grid):
                        if grid[r+1][c] == 0:
                            curr_bounds.add((r+1,c))
                        elif grid[r+1][c] == 1:
                            curr_size += 1
                            grid[r+1][c] = -1
                            queue.append((r+1, c))
                    if c+1<len(grid[i]):
                        if grid[r][c+1] == 0:
                            curr_bounds.add((r,c+1))
                        elif grid[r][c+1] == 1:
                            curr_size += 1
                            grid[r][c+1] = -1
                            queue.append((r, c+1))
                best_join = 0
                
                for loc in curr_bounds:
                    if loc in bounds:
                        best_join = max(bounds[loc], best_join)
                        bounds[loc] += curr_size
                    else:
                        bounds[loc] = curr_size
                res = max(res, best_join+curr_size+1 if curr_bounds else curr_size)
        return res
                
        