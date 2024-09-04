class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        mix = [[positions[i], healths[i], i] for i in range(len(healths))]
        mix.sort()
        right = []
        left = []
        for p, h, i in mix:
            if directions[i] == 'R':
                right.append([i, h])
            else:
                while right and h and right[-1][1] < h:
                    right.pop()
                    h -= 1

                if right and h == right[-1][1]:
                    right.pop()
                    continue
                elif right:
                    right[-1][1] -= 1
                else:
                    left.append([i, h])
        

        survivors = right + left
        survivors.sort()
        survivors = [h for i, h in survivors]
        return survivors
        
                    

