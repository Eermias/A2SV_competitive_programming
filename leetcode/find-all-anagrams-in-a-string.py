class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        mapp1 = {}
        for c in p:
            mapp1[c] = 1 + mapp1.get(c, 0)
        mapp2 = {}
        l = 0
        r = 0
        while r < len(p):
            mapp2[s[r]] = 1 + mapp2.get(s[r], 0)
            r += 1
        r -= 1
        res = []
        while r < len(s):
            if mapp1 == mapp2:
                res.append(l)
            r += 1
            l += 1
            if r < len(s):
                mapp2[s[r]] = 1 + mapp2.get(s[r], 0)
                if mapp2[s[l - 1]] == 1:
                    mapp2.pop(s[l - 1])
                else:
                    mapp2[s[l - 1]] -= 1

        return res


        