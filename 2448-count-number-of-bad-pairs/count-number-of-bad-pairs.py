class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        n = len(nums)

        count = defaultdict(int)
        for i in range(n):
            count[nums[i] - i] += 1
        
        total = (n * (n - 1)) // 2
        good_pairs = 0
        for val, cnt in count.items():
            good_pairs += (cnt * (cnt - 1)) // 2
        
        return total - good_pairs