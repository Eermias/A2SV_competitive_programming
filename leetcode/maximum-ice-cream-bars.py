class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        count = 0
        for i in range(len(costs)):
            if coins >= costs[i]:
                count += 1
                coins -= costs[i]
                print(coins)
            else:
                break
        
        return count
        