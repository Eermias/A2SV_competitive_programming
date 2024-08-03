class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                #if nums[m] is in the left rotated portion
                if nums[r] <= nums[l] <= nums[m]:
                    l = m + 1
                else:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                #if nums[m] is in the left rotated portion
                if nums[m] <= nums[r] <= nums[l]:
                    r = m - 1
                else:
                    if target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1

        return -1
