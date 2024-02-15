class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #BRUTE FORCE
        #count = 0

        #for i in range(len(nums)):
         #   for j in range(i+1,len(nums)):
          #      if (j * i) % k == 0 and nums[j] == nums[i]:
           #         count += 1
        #return count

        hashmap = {}
        count = 0

        for i in range(len(nums)):
            if nums[i] in hashmap:
                for j in hashmap[nums[i]]:
                    if (j*i)%k == 0:
                        count += 1
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]
        return count
