class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        prev = defaultdict(int)
        count = 0
        for hr in hours:
            mod = hr % 24
            target = (24 - mod) % 24
            count += prev[target]
            prev[mod] += 1
        
        return count