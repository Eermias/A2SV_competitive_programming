class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr = []
        def backtrack(i, curr_sum):
            if curr_sum == target:
                result.append(curr[:])
                return
            if curr_sum > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, curr_sum + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr_sum)
        
        backtrack(0, 0)
        return result