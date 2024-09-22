class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        count = Counter(nums)
        nums = list(set(nums))

        perms = []
        def backtrack(curr):
            if len(curr) == n:
                perms.append(curr[:])
                return
            
            for i in range(len(nums)):
                if count[nums[i]] > 0:
                    curr.append(nums[i])
                    count[nums[i]] -= 1
                    backtrack(curr)

                    curr.pop()
                    count[nums[i]] += 1
        
        backtrack([])
        return perms
