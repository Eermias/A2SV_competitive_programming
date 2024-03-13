# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            version = (l + r) // 2
            if isBadVersion(version):
                first_bad = version
                r = version - 1
            else:
                l = version + 1

        return first_bad
