class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        curr = []
        used = set()
        def backtrack():
            if len(curr) == len(nums):
                perms.append(curr[:])
                return
            
            for n in nums:
                if n not in used:
                    curr.append(n)
                    used.add(n)
                    backtrack()
                    curr.pop()
                    used.remove(n)
        
        backtrack()
        return perms