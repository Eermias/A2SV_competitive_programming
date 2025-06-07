class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf") 
        curr_min, curr_max = 1, 1
        for n in nums:
            temp = curr_min
            curr_min = min(curr_min * n, curr_max * n, n) 
            curr_max = max(curr_max * n, temp * n, n)
            max_product = max(max_product, curr_max)
        return max_product

        
        