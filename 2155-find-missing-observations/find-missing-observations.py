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
                if more >= 5:
                    ans[i] += 5
                    more -= 5
                else:
                    ans[i] += more
                    break
            
            return ans