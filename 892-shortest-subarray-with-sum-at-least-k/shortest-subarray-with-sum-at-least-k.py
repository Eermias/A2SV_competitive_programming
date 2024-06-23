class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        window = deque()
        window.append([-1, 0])
        curr_sum = 0
        shortest = float("inf")
        for i, n in enumerate(nums):
            curr_sum += n
            while window and curr_sum <= window[-1][1]:
                window.pop()
            #print(window)
            
            while window and curr_sum - window[0][1] >= k:
                idx, prefix = window.popleft()
                shortest = min(shortest, i - idx)
            window.append([i, curr_sum])

        return shortest if shortest != float("inf") else -1

