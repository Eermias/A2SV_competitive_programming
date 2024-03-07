class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        def isBalanced():
            for key in count:
                if count[key] > n/4:
                    return False
            return True

        l, r = 0, 0
        res = n
        while r < len(s) :
            if not isBalanced():
                count[s[r]] -= 1
                r += 1
            while isBalanced():
                res = min(res, r - l)
                if res == 0:
                    return res
                count[s[l]] += 1
                l += 1
        
        return res
        

            
                




       