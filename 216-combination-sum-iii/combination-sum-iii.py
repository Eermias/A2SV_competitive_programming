class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(i, curr_sum):
            if len(curr) == k:
                if curr_sum == n:
                    result.append(curr[:])
                return 
            if i > 9:
                return
            
            curr.append(i)
            backtrack(i + 1, curr_sum + i)
            curr.pop()
            backtrack(i + 1, curr_sum)
        
        backtrack(1, 0)
        return result
            