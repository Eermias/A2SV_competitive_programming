class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #replace odds by 1's and evens by 0's
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        index = [-1]
        for i in range(len(nums)):
            if nums[i] == 1:
                index.append(i)
        index.append(len(nums))

        l, r = 1, k
        total = 0
        while r < len(index) - 1:
            total += (index[l]-index[l-1]) * (index[r+1]-index[r])
            l += 1
            r += 1
        return total




        

