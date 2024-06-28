class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def pick(l, r):
            if l > r:
                return 0
            left = nums[l] - pick(l + 1, r)
            right = nums[r] - pick(l, r - 1)
            
            return max(left, right)
        
        if pick(0, len(nums) - 1) >= 0:
            return True
        return False
