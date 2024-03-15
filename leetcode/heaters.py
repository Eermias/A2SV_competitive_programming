class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        min_rad = 0
        for house in houses:
            closest = 10 ** 9
            l, r = 0, len(heaters) - 1
            while l <= r:
                m = (l + r) // 2
                dis = abs(house - heaters[m])
                closest = min(closest, dis)
                if house == heaters[m]:
                    break
                elif house > heaters[m]:
                    l = m + 1
                else:
                    r = m - 1
            min_rad = max(min_rad, closest)
        
        return min_rad

        