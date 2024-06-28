class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [[float("-inf"), -1]]
        min_sum = 0
        for i, n in enumerate(arr):    
            while stack and stack[-1][0] > n:
                num, idx = stack.pop()
                min_sum += (i - idx) * (idx - stack[-1][1]) * num
            
            stack.append([n, i])
            
        for i in range(1, len(stack)):
            num, idx = stack[i]
            min_sum += (len(arr) - idx) * (idx - stack[i - 1][1]) * num

        return min_sum % (10**9 + 7)