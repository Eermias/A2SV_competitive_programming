class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        n = len(nums)

        count = defaultdict(int)

        for i in range(n):
            for j in range(n):
                if i != j:
                    count[nums[i] * nums[j]] += 1
        
        ans = 0
        for product, cnt in count.items():
            ans += max(0, cnt * (cnt - 2))
        
        return ans