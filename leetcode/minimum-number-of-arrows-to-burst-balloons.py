class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        mapp = defaultdict(list) #end : start
        shots = []
        for pair in points:
            mapp[pair[1]].append(pair[0])
            shots.append(pair[1])
        count = 0
        shots.sort()
        #print(mapp, shots)
        prevShot = float("-inf")
        for i in range(len(points)):
            #print(mapp[shots[i]].pop())
            if mapp[shots[i]].pop() > prevShot:
                prevShot = shots[i]
                count += 1
            

        return count
        