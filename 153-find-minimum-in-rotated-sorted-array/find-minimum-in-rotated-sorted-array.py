class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minn = nums[0]
        while l <= r:
            m = (l + r) // 2
            minn = min(minn, nums[m])
            #m in left rotated portion
            if nums[m] > nums[r]:
                l = m + 1
                
            #m in right rotated portion
            else:
                r = m - 1
        return minn

        
        
        
        
        
        
        
        
        
        """l, r = 0, len(nums) - 1
        min_num = nums[0] #assign any number from the array
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] <= nums[r]: #sorted version
                min_num = min(min_num, nums[l])
                r = mid - 1
            elif nums[mid] >= nums[r] and nums[mid] >= nums[l]:
                min_num = min(min_num, nums[r])
                l = mid + 1
            else:
                min_num = min(min_num, nums[mid])
                r = mid - 1
        
        return min_num"""

        