class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        while numBottles >= numExchange:
            drunk += numExchange
            numBottles -= numExchange - 1
        
        drunk += numBottles
        return drunk