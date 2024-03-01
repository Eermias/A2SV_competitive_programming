class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        max_processing_time = 0
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(tasks):
            max_processing_time = max(max_processing_time, processorTime[ptr1] + tasks[ptr2])
            ptr1 += 1
            ptr2 += 4

        return max_processing_time

        