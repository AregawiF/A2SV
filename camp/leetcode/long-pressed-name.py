class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        p2 = 0
        while p1 < len(name) and p2 < len(typed):
            if name[0] != typed[0]:
                return False 
            if name[p1] != typed[p2]:
                if typed[p2] != name[p1-1]:
                    return False
                p2 += 1
            else:
                p1 += 1
                p2 +=1
        while p2 < len(typed):
            if typed[p2] != name[-1]:
                return False
            else:
                p2+=1
        if p1 != len(name):
            return False
        return True