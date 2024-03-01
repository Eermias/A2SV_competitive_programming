class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        skill.sort()
        total = skill[0] + skill[-1]
        l = 0
        r = len(skill) - 1
        while l < r:
            groupSkill = skill[l] + skill[r]
            if groupSkill != total:
                return -1
            chemistry += (skill[r] * skill[l])
            l += 1
            r -= 1

        return chemistry

        