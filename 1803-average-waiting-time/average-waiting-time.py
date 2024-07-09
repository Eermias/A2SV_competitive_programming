class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        for i in range(len(customers)):
            customers[i][1] += customers[i][0]
            if i > 0:
                customers[i][1] += max(0, customers[i - 1][1] - customers[i][0])
            
            total += customers[i][1] - customers[i][0]
        
        return total / len(customers)
