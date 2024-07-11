class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, max_profit = 0, 0
        for r in range(len(prices)):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        
        return max_profit