class Solution:
    def longestPalindrome(self, s: str) -> int:
        centerFilled = False
        count = {} #letter : occurence
        for char in s:
            count[char] = 1 + count.get(char, 0)
        maxLen = 0
        for key in count:
            if count[key] % 2 == 0:
                maxLen += count[key]
            else:
                if not centerFilled:
                    maxLen += count[key]
                    centerFilled = True
                else:
                    maxLen += count[key] - (count[key] % 2)
        return maxLen
        