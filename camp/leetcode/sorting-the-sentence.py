class Solution:
    def sortSentence(self, s: str) -> str:
        mylist = list(s.split())
        mylist.sort(key= lambda x: x[-1])
        result = ""
        for word in mylist:
            result += word[:-1] 
            if word != mylist[-1]:
                result += " "
        return result