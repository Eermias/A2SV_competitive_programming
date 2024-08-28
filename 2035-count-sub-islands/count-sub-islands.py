class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            ans = True
            if grid1[r][c] == 0:
                ans = False

            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = r + dr
                y = c + dc
                if -1 < x < len(grid1) and -1 < y < len(grid1[0]):
                    if grid2[x][y] == 1 and (x, y) not in visited:
                        ans = dfs(x, y) and ans
            
            return ans
        
        visited = set()
        sub_islands = 0
        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                if grid2[r][c] == 1 and (r, c) not in visited and dfs(r, c):
                    sub_islands += 1
                    #print(r, c, visited)
        
        return sub_islands