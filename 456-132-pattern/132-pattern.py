class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        pre_max = -math.inf
        for num in nums[::-1]:
            if num < pre_max: return True
            while stack and stack[-1]<  num:
                # pre_max = max(pre_max, stack.pop())
                pre_max =  stack.pop()
            stack.append(num)  
        return False