class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            condition1 = firstList[ptr1][0] <= secondList[ptr2][1]
            condition2 = secondList[ptr2][0] <= firstList[ptr1][1]
            if condition1 and condition2: #there is intersection
                intersection.append([max(firstList[ptr1][0], secondList[ptr2][0]), min(firstList[ptr1][1], secondList[ptr2][1])])
            #which ptr moves?
            if firstList[ptr1][1] <= secondList[ptr2][1]:
                ptr1 += 1
            else:
                ptr2 += 1
        
        return intersection
        