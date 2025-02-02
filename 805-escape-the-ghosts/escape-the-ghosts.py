class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        shortest = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            time = abs(target[0] - x) + abs(target[1] - y)
            if time <= shortest:
                return False
        
        return True
        

            

