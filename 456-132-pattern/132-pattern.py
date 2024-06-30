class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #[num, min_popped]

        for n in nums:
            minn = n
            while stack and stack[-1][0] <= n:
                num, min_pop = stack.pop()
                minn = min(minn, min_pop)
            
            for i in range(len(stack) - 1, -1, -1):
                if stack[i][0] == stack[i][1]:
                    continue
                if stack[-1][1] < n:
                    #print(stack)
                    return True
            stack.append([n, minn])
        
        return False


