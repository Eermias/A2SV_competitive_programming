class Solution(object):
    def topKFrequent(self, nums, k):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        paired = [[f, n] for n, f in count.items()]
        paired.sort(reverse = True)
        ans = []
        for i in range(k):
            ans.append(paired[i][1])
        
        return ans
        