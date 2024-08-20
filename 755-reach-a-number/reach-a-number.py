class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        low, high = 0, 2 * target
        ans = high
        while low <= high:
            mid = (low + high) // 2
            dest = (mid * (mid + 1)) // 2
            if dest < target:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        
        dest = (ans * (ans + 1)) // 2
        while (dest - target) % 2:
            ans += 1
            dest = (ans * (ans + 1)) // 2
            
        return ans