class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                if nums[l] >= nums[r] >= nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                
                else:
                    l = m + 1
            else:
                if nums[m] >= nums[l] >= nums[r]:
                    if target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                
                else:
                    r = m - 1
        return -1