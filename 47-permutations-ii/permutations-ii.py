class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        perms = []
        mask = 0
        def backtrack(curr):
            if len(curr) == len(nums):
                perms.append(curr[:])
                return
            
            nonlocal mask
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and mask & (1 << (i - 1)) == 0:
                    continue
                elif mask & (1 << i) == 0:
                    curr.append(nums[i])
                    mask |= (1 << i)
                    backtrack(curr)

                    curr.pop()
                    mask ^= (1 << i)
        
        backtrack([])
        return perms
