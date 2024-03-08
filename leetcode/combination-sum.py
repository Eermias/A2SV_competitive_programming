class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, curr, total):
            if total > target:
                return
            if idx == len(candidates):
                if total == target:
                    res.append(curr[:])
                return
            curr.append(candidates[idx])
            total += candidates[idx]
            dfs(idx, curr, total)

            curr.pop()
            total -= candidates[idx]
            dfs(idx + 1, curr, total)

        dfs(0, [], 0)
        return res

                
        