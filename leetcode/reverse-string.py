class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rec(l,r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            rec(l + 1, r - 1)
        rec(0, len(s) -1)

        

        