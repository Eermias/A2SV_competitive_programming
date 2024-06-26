class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mix = [[difficulty[i], profit[i]] for i in range(len(profit))]
        mix.sort()
        worker.sort()
        heap = []
        
        max_profit = 0
        ptr1, ptr2 = 0, 0
        while ptr1 < len(worker) and ptr2 < len(mix):
            if worker[ptr1] >= mix[ptr2][0]:
                heapq.heappush(heap, -mix[ptr2][1])
                ptr2 += 1
            else:
                ptr1 += 1
                if not heap:
                    continue
                max_profit += -heap[0]
                
        if ptr1 < len(worker):
            max_profit += (len(worker) - ptr1) * (-heap[0])
        
        return max_profit