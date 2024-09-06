class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        min_total = sum(rolls) + n
        more = mean * (m + n) - min_total
        if more < 0 or more > 5 * n:
            return []
        else:
            ans = [1] * n
            for i in range(n):
                minn = min(more, 5)
                ans[i] += minn
                more -= minn
            
            return ans