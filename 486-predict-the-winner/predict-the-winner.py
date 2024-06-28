class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)] #row = l, col = r
        for i in range(n):
            dp[i][i] = nums[i]
        
        for d in range(1, n):
            for l in range(n - d):
                r = l + d
                left = nums[l] - dp[l + 1][r]
                right = nums[r] - dp[l][r - 1]
                dp[l][r] = max(left, right)
        
        #print(dp)
        if dp[0][n - 1] >= 0:
            return True
        return False
