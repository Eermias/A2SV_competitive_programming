class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mix = [[difficulty[i], profit[i]] for i in range(len(profit))]
        mix.sort()
        worker.sort()

        best_job = 0
        max_profit = 0
        ptr = 0
        for i in range(len(worker)):
            while ptr < len(mix) and mix[ptr][0] <= worker[i]:
                best_job = max(best_job, mix[ptr][1])
                ptr += 1
            max_profit += best_job
            
        return max_profit