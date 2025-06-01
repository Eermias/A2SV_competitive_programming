class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        prev, curr = cost[0], cost[1]
        for i in range(2, len(cost)):
            best = cost[i] + min(prev, curr)
            prev = curr
            curr = best
        
        return curr