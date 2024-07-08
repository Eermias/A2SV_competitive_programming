class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                #left rotated portion --> right
                if nums[m] >= nums[l] >= nums[r]:
                    l = m + 1
                #right rotated portion --> right or left
                elif nums[l] >= nums[r] >= nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                #normal --> right
                else:
                    l = m + 1
            else:
                #left rotated portion --> right
                if nums[m] >= nums[l] >= nums[r]:
                    if target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                #right rotated portion --> right or left
                elif nums[l] >= nums[r] >= nums[m]:
                    r = m - 1
                #normal --> right
                else:
                    r = m - 1
        return -1