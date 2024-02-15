class Solution:
    def maxScore(self, s: str) -> int:
        leftScore = [0]
        rightScore = [0]
        for i,c in enumerate(s):
            leftScore.append(int(c == "0"))
            leftScore[i + 1] += leftScore[i]
        for i,c in enumerate(reversed(s)):
            rightScore.append(int(c == "1"))
            rightScore[i + 1] += rightScore[i]
        rightScore.reverse()
        max_score = float("-inf")
        for i in range(1,len(rightScore) - 1):
            curr_score = rightScore[i] + leftScore[i]
            max_score = max(max_score, curr_score)
        return max_score



        