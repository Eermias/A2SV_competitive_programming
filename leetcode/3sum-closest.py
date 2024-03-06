class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            a = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = a + nums[l] + nums[r]
                if abs(summ - target) < abs(res - target):
                        res = summ
                if summ == target:
                    return summ
                elif summ < target:
                    l += 1
                else:
                    r -= 1
        
        return res
                
                    

        
        return res

