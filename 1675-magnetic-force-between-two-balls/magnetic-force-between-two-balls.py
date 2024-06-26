class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def get_next(nxt):
            l, r = 0, len(position) - 1
            idx = float("inf")
            while l <= r:
                m = (l + r) // 2
                if position[m] >= nxt:
                    idx = m
                    r = m - 1
                else:
                    l = m + 1
            return idx
        
        def is_possible(mid):
            count = 1
            prev = 0
            while count < m:
                nxt = position[prev] + mid
                prev = get_next(nxt)
                if prev == float("inf"):
                    return False
                else:
                    count += 1
            return True


        position.sort()
        low, high = 0, max(position)
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if is_possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


