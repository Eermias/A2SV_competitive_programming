class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(i, path, curr_sum):
            if curr_sum == target:
                result.append(path[:])
                return
            
            if i == len(candidates) or curr_sum > target:
                return
            
            path.append(candidates[i])
            backtrack(i + 1, path, curr_sum + candidates[i])

            path.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            backtrack(i + 1, path, curr_sum)
        
        backtrack(0, [], 0)
        return result

