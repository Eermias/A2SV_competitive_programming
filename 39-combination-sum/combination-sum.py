class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(i, picked):
            if sum(picked) == target:
                result.append(picked[:])
                return
            if i == len(candidates) or sum(picked) > target:
                return
            
            backtrack(i + 1, picked)
            picked.append(candidates[i])
            backtrack(i, picked)
            picked.pop()
        
        backtrack(0, [])
        return result
            

            
                
        