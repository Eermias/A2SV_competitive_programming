class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = 1
        moves = 0
        double = [target]
        for i in range(maxDoubles):
            if double[-1] <= 3:
                break
            double.append(double[-1]//2)
        print(double)
        while curr != target:
            moves += double[-1] - curr
            curr = double.pop()
            if curr != target:
                curr *= 2
                moves += 1
        return moves


        
        