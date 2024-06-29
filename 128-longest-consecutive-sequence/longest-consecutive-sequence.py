class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)

        longest = 0
        while sett:
            n = sett.pop()
            smaller = 0
            l = n - 1
            while l in sett:
                sett.remove(l)
                l -= 1
                smaller += 1
            
            larger = 0
            r = n + 1
            while r in sett:
                sett.remove(r)
                r += 1
                larger += 1
            
            longest = max(longest, smaller + larger + 1)
        
        return longest