class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        myCoins = 0
        piles.sort(reverse = True)
        me = 1
        bob = len(piles) - 1
        while me < bob:
            myCoins += piles[me]
            me += 2
            bob -= 1
        
        return myCoins
        