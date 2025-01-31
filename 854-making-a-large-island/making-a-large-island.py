class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                if size[root1] >= size[root2]:
                    parent[root2] = root1
                    size[root1] += size[root2]
                else:
                    parent[root1] = root2 
                    size[root2] += size[root1]

        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        parent = {}
        size = {}
        for r in range(n):
            for c in range(n):
                parent[(r, c)] = (r, c)
                size[(r, c)] = 1 if grid[r][c] == 1 else 0

        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        nr = r + dr
                        nc = c + dc
                        if -1 < nr < n and -1 < nc < n:
                            if grid[nr][nc] == 1:
                                union((r, c), (nr, nc))

        ans = max(size.values())
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    max1, max2, max3, max4 = 0, 0, 0, 0
                    roots = []
                    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        nr = r + dr
                        nc = c + dc
                        
                        if -1 < nr < n and -1 < nc < n:
                            roots.append(find((nr, nc)))
                        
                    roots = list(set(roots))
                    
                    for root in roots:
                        if size[root] > max1:
                            max4 = max3
                            max3 = max2
                            max2 = max1
                            max1 = size[root]
                        elif size[root] > max2:
                            max4 = max3
                            max3 = max2
                            max2 = size[root]
                        elif size[root] > max3:
                            max4 = max3
                            max3 = size[root]
                        elif size[root] > max4:
                            max4 = size[root]
                    
                    ans = max(ans, max1 + max2 + max3 + max4 + 1)

        return ans



