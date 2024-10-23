class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle) + 1):
            temp = haystack[i:i+len(needle)]
            
            if needle == temp:
                return i
        return -1