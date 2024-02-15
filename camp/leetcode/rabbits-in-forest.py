class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        my_dict = defaultdict(int)
        result = 0
        for ans in answers:
            my_dict[ans] += 1
        for key, val in my_dict.items():
            res = math.ceil(val/(key+1))
            result += res * (key+1)
        return result