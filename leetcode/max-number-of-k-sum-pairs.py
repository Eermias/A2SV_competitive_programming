class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        ptrL = 0
        ptrR = len(nums) - 1
        while ptrL < ptrR:
            summ = nums[ptrL] + nums[ptrR]
            if summ == k:
                count += 1
                ptrL += 1
                ptrR -= 1
            elif summ > k:
                ptrR -= 1
            else:
                ptrL += 1

        return count


        