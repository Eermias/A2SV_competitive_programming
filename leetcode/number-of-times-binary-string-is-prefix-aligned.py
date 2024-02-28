class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        curr_max = 0
        count = 0
        for i in range(len(flips)):
            curr_max = max(curr_max, flips[i])
            if curr_max == i + 1:
                count += 1
        return count

        