class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        mix = [[positions[i], healths[i], i] for i in range(len(healths))]
        mix.sort()
        survivors = []
        for p, h, i in mix:
            if directions[i] == "R":
                survivors.append([p, h, i])
            else:
                while survivors and directions[survivors[-1][2]] == "R" and survivors[-1][1] < h:
                    survivors.pop()
                    h -= 1
                if not h:
                    continue
                elif not survivors:
                    survivors.append([p, h, i])
                else:
                    dxn = directions[survivors[-1][2]]
                    hlth = survivors[-1][1]
                    if dxn == "L":
                        survivors.append([p, h, i])
                    elif hlth > h:
                        survivors[-1][1] -= 1
                        continue
                    elif hlth == h:
                        survivors.pop()
                        continue
        survivors.sort(key = lambda x:x[2])
        result = [survivors[i][1] for i in range(len(survivors))]
        return result
        
                    

