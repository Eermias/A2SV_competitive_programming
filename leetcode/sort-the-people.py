class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapp = {} #height : name
        for i in range(len(heights)):
            mapp[heights[i]] = names[i]
        heights.sort(reverse = True)
        for i in range(len(names)):
            names[i] = mapp[heights[i]]
        
        return names
        