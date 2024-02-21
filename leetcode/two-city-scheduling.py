class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        mapp = defaultdict(list) #profit : val
        for i in range(len(costs)):
            profit = costs[i][0] - costs[i][1]
            diff.append(profit)
            mapp[profit].append(i)
        for key in mapp:
            arr = []
            while mapp[key]:
                arr.append(mapp[key].pop())  
            mapp[key] += arr 
        diff.sort()
        minCost = 0
        mid = len(costs)//2
        print(diff, mapp)
        for i in range(len(costs)):
            index = mapp[diff[i]].pop()
            if i < mid:
                minCost += costs[index][0]
            else:
                minCost += costs[index][1]

        return minCost

            
