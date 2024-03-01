class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        l = 0
        count = 0
        maxx = 0
        for r in range(k):
            if s[r] in vowels:
                count += 1
        maxx = max(count, maxx)
        r = k
        while r < len(s):
            if s[r] in vowels:
                count += 1
            if s[l] in vowels:
                count -= 1
            r += 1
            l += 1
            maxx = max(maxx, count)
        return maxx

            

        