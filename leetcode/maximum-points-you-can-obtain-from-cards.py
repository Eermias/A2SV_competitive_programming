class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        picked = 0
        l = 0
        r = len(cardPoints) - 1
        for i in range(k):
            picked += cardPoints[i]
            l = i
        maxPicked = picked
        while k:
            picked = picked - cardPoints[l] + cardPoints[r]
            r -= 1
            l -= 1
            k -= 1
            maxPicked = max(maxPicked, picked)

        return maxPicked

                
        