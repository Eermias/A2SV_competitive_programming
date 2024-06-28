class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [[float("-inf"), -1]]
        min_sum = 0
        for i, n in enumerate(arr):    
            while stack and stack[-1][0] > n:
                num, idx = stack.pop()
                left = i - idx
                right = idx - stack[-1][1]
                min_sum += left * right * num
            
            stack.append([n, i])
            
        for i in range(1, len(stack)):
            num, idx = stack[i]
            left = len(arr) - idx
            right = idx - stack[i - 1][1]
            min_sum += left * right * num

        return min_sum % (10**9 + 7)