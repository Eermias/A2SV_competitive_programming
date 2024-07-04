class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        trapped = 0
        while l <= r:
            if left_max >= right_max:
                trapped += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
                r -= 1
            else:
                trapped += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
                l += 1
        
        return trapped

