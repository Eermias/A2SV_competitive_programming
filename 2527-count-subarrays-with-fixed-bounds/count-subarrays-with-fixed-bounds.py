class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minn = []
        maxx = []
        count = 0
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                minn = []
                maxx = []
                continue

            last = i
            while minn and nums[minn[-1][1]] >= nums[i]:
                prev, idx = minn.pop()
                last = prev

            minn.append((last, i))

            last = i
            while maxx and nums[maxx[-1][1]] <= nums[i]:
                prev, idx = maxx.pop()
                last = prev
            maxx.append((last, i))

            # print('minn')
            # print(minn)
            # print('maxx')
            # print(maxx)
            if minn and nums[minn[0][1]] == minK and maxx and nums[maxx[0][1]] == maxK:
                if minn[0][1] < maxx[0][1]:
                    count += minn[0][1] - minn[0][0] + 1
                else:
                    count += maxx[0][1] - maxx[0][0] + 1
        
        return count
