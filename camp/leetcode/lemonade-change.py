class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        twenys = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                tens+=1
                if fives == 0:
                    return False
                else:
                    fives -= 1
            else:
                twenys += 1
                if fives == 0:
                    return False
                elif tens == 0 and fives < 3:
                    return False
                elif tens == 0 and fives >= 3:
                    fives-=3
                else:
                    tens-=1
                    fives-=1
        return True