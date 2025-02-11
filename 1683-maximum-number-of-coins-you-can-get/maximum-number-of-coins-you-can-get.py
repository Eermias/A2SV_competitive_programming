class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles) // 3
        piles.sort()
        result = 0
        for i in range(n, len(piles), 2):
            result += piles[i]
        return result
