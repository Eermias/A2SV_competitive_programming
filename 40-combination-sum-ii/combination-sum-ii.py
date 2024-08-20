class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr = []
        def backtrack(i, summ):
            if i == len(candidates) or summ >= target:
                if summ == target:
                    result.append(curr[:])
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, summ + candidates[i])
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            curr.pop()
            backtrack(j, summ)
        
        backtrack(0, 0)
        return result