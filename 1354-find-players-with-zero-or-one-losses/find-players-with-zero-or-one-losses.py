class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = defaultdict(int)
        for winner, loser in matches:
            count[loser] += 1
            count[winner] += 0
        
        ans = [[],[]]
        for player in count:
            if count[player] == 0:
                ans[0].append(player)
            elif count[player] == 1:
                ans[1].append(player)
                
        ans[0].sort()
        ans[1].sort()
        return ans