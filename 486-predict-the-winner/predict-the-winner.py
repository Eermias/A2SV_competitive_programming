class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def pick(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            left = nums[l] - pick(l + 1, r)
            right = nums[r] - pick(l, r - 1)
            
            memo[(l, r)] = max(left, right)
            return memo[(l, r)]
        
        if pick(0, len(nums) - 1) >= 0:
            return True
        return False
