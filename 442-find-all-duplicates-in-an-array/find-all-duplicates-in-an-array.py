class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ptr = 0
        while ptr < len(nums):
            if nums[ptr] == ptr + 1:
                ptr += 1
            else:
                pos = nums[ptr] - 1
                if nums[pos] == nums[ptr]:
                    ptr += 1
                else:
                    nums[ptr], nums[pos] = nums[pos], nums[ptr]
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        
        return res
        