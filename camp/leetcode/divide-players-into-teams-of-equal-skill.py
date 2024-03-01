class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        chem = 0
        skill.sort()
        n = len(skill)
        team = skill[0] + skill[n-1]
        for i in range(len(skill)//2):
            if skill[i] + skill[n-1-i] != team:
                return -1

        for i in range(len(skill)//2):
            chem += skill[i] * skill[n-1-i]
        

        return chem