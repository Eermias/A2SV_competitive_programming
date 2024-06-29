class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)

        longest = 0
        for n in nums:
            if n - 1 in sett:
                continue
            else:
                count = 0
                i = n
                while i in sett:
                    count += 1
                    i += 1
                longest = max(longest, count)
        
        return longest