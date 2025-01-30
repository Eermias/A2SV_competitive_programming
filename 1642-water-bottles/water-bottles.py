class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        while numBottles >= numExchange:
            drunk += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        
        return drunk

