class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        n = len(nums)

        good_pairs = defaultdict(int)
        for i in range(n):
            good_pairs[nums[i] - i] += 1
        
        bad_pairs = (n * (n - 1)) // 2
        for value, count in good_pairs.items():
            bad_pairs -= (count * (count - 1)) // 2
        
        return bad_pairs