class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(i, curr_sum):
            if curr_sum == target:
                result.append(curr[:])
                return
            if curr_sum > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            curr.pop()
            backtrack(i + 1, curr_sum)
        
        backtrack(0, 0)
        return result
            

            
                
        