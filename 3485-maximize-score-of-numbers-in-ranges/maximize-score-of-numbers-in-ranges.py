class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def possible(gap):

            prev = start[0]
            for i in range(1, len(start)):
                if prev + gap <= start[i] + d:
                    prev = max(prev + gap, start[i])
                else:
                    return False

            return True

        low, high = 0, start[-1] + d - start[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
