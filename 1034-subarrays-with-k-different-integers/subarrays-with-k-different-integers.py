class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def get_count(limit):
            counter = {}
            l = 0
            count = 0
            for r in range(n):
                counter[nums[r]] = 1 + counter.get(nums[r], 0)
                while len(counter) > limit:
                    counter[nums[l]] -= 1
                    if counter[nums[l]] == 0:
                        counter.pop(nums[l])
                    l += 1
                count += r - l + 1
            
            return count
        
        n = len(nums)
        return get_count(k) - get_count(k - 1)