class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        low, high = 0, start[-1] + d - start[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            prev = start[0]
            possible = True
            for i in range(1, len(start)):
                if prev + mid <= start[i] + d:
                    prev = max(prev + mid, start[i])
                else:
                    possible = False
                    break
            
            if possible:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
