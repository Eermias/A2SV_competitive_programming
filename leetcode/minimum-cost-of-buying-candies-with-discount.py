class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        price = 0
        idx = 2
        for i in range(len(cost)):
            if i != idx:
                price += cost[i]
            else:
                idx += 3
        return price
        