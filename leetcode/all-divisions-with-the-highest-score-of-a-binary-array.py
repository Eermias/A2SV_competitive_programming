class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        onesTotal = 0
        zerosTotal = 0
        for n in nums:
            if n == 0:
                zerosTotal += 1
            else:
                onesTotal += 1

        mapp = defaultdict(list)        
        ones = 0
        zeros = 0
        for i in range(len(nums)):
            score = zeros + onesTotal - ones
            mapp[score].append(i)
            if nums[i] == 0:
                zeros += 1    
            else:
                ones += 1
        mapp[zerosTotal].append(len(nums))
        maxx = max(mapp)

        return mapp[maxx]



        