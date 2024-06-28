class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []
        min_sum = 0
        for i, n in enumerate(arr):    
            while stack and stack[-1][0] > n:
                num, idx = stack.pop()
                min_sum += (i - idx) * (idx - stack[-1][1]) * num
            
            stack.append([n, i])
            
        return min_sum % (10**9 + 7)