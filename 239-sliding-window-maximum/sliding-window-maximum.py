class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()
        for i in range(k - 1):
            while candidates and candidates[-1] < nums[i]:
                candidates.pop()
            candidates.append(nums[i])
        
        output = []
        l, r = 0, k - 1
        while r < len(nums):
            while candidates and candidates[-1] < nums[r]:
                candidates.pop()
            candidates.append(nums[r])
            output.append(candidates[0])
            if nums[l] == candidates[0]:
                candidates.popleft()
            r += 1
            l += 1
        
        return output

        
        
        



        

