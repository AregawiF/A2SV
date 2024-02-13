class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = {}
        for i in range(len(names)):
            name = names[i]
            height = heights[i]
            if name in people:
                people[name].append(height) 
            else:
                people[name] = [height]  

        heights.sort(reverse = True)
        result = []

        def getval(height):
            name = [i for i in people if height in people[i]]
            return name

        for height in heights:
            result.extend(getval(height))
        return result
        
