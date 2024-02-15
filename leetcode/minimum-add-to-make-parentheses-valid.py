class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        minAdd = 0
        countOpen = 0
        for p in s:
            if p == "(":
                countOpen += 1
            else:
                if countOpen:
                    countOpen -= 1
                else:
                    minAdd += 1
        return minAdd + countOpen