class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = {0:1} #num[index] % 5 : count
        summ = 0
        count = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ % k in remainders:
                count += remainders[summ % k]
            remainders[summ % k] = 1 + remainders.get(summ % k, 0)
        return count


        