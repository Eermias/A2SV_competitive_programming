class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        
        count.sort(reverse = True)
        pushes = 0
        for i in range(26):
            times = 1 + (i) // 8
            pushes += count[i] * times
        
        return pushes
