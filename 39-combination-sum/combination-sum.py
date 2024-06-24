class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        picked = []
        def backtrack(i, curr):
            if curr == target:
                result.append(picked[:])
                return
            if i == len(candidates) or curr > target:
                return
            
            backtrack(i + 1, curr)
            picked.append(candidates[i])
            backtrack(i, curr + candidates[i])
            picked.pop()
        
        backtrack(0, 0)
        return result
            

            
                
        