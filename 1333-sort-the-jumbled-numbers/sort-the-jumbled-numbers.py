class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = [str(n) for n in mapping]
        def mapp(num):
            num = str(num)
            res = ""
            for n in num:
                res += mapping[int(n)]
            return int(res)
        
        nums = [[mapp(nums[i]), i, nums[i]] for i in range(len(nums))]
        nums.sort()
        result = [nums[i][2] for i in range(len(nums))]
        return result