class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        group = {}
        for ans in answers:
            if ans == 0:
                count += 1
            elif ans in group and group[ans] > ans:
                count += (ans + 1)
                group[ans] = 1 
            else:
                group[ans] = 1 + group.get(ans, 0)
        for key in group:
            count += (key + 1)

        return count 
        