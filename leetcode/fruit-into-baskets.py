class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        types = {}
        maxx = 0
        l, r = 0, 0
        for r in range(len(fruits)):
            f = fruits[r]
            types[f] = 1 + types.get(f, 0)
            if len(types) <= 2:
                maxx = max(maxx, r-l + 1)
            else:
                while len(types) > 2:
                    types[fruits[l]] -= 1
                    if types[fruits[l]] == 0:
                        types.pop(fruits[l])
                    l += 1
        return maxx

            


            



        