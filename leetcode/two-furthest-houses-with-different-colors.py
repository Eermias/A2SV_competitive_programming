class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxGap = 0
        for i in range(len(colors)):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    maxGap = max(maxGap, j - i)
        return maxGap
        