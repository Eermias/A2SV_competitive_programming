class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashChars = {}
        left = 0
        right = 0
        longest = 0

        while right < len(s):
            if s[right] not in hashChars:
                hashChars[s[right]] = None
                right += 1
            else:
                while s[right] in hashChars:
                    hashChars.pop(s[left])
                    left += 1
                hashChars[s[right]] = None
                right += 1
            longest = max(longest, right - left)
        return longest
            

        

        