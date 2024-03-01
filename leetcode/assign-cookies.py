class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed = g
        satisfied = s
        greed.sort()
        s.sort()
        ptr1 = 0
        ptr2 = 0
        count = 0
        while ptr1 < len(greed) and ptr2 < len(satisfied):
            if greed[ptr1] <= satisfied[ptr2]:
                count += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1

        return count

        