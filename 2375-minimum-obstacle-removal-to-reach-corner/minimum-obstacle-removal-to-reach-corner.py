class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        processed = set()

        def inbound(i,j):
            return 0 <= i < m and 0 <= j < n
        
        d = [(0,1),(0,-1),(1,0),(-1,0)]

        heap = [(0,0,0)]
        

        while heap:
            dis, posx, posy = heappop(heap)
            for x,y in d:
                if inbound(posx + x,posy + y) and (posx + x,posy + y) not in processed:
                    processed.add((posx + x,posy + y))
                    heappush(heap,(dis + grid[posx + x][posy + y],posx + x,posy + y))
                
                if posx + x == m - 1 and posy + y == n - 1:
                    return dis
        
        return dis