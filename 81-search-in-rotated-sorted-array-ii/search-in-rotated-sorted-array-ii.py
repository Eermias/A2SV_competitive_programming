class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[l] == nums[m] == nums[r]:
                return self.search(nums[l : m], target) or self.search(nums[m + 1 : r + 1], target)
            elif nums[m] < target:
                #check if nums[m] is in the left rotated portion
                if nums[r] <= nums[l] <= nums[m]:
                    l = m + 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                #check if nums[m] is in the left rotated portion
                if nums[r] <= nums[l] <= nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
        
        return False

