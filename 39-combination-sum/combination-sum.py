class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(i, summ):
            if i == len(candidates) or summ >= target:
                if summ == target:
                    result.append(curr[:])
                return
            
            curr.append(candidates[i])
            backtrack(i, summ + candidates[i])

            curr.pop()
            backtrack(i + 1, summ)
        
        backtrack(0, 0)
        return result