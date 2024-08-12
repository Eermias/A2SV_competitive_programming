class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # compute the maximum and minimum values
        max_value, min_value = max(nums), min(nums)
        
        # compute the size of each bucket
        bucket_size = max(1, (max_value - min_value) // (n - 1))
        
        # compute the number of buckets
        num_buckets = (max_value - min_value) // bucket_size + 1
        
        # initialize the buckets with maximum and minimum values
        buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]
        for num in nums:
            bucket_index = (num - min_value) // bucket_size
            buckets[bucket_index][0] = min(buckets[bucket_index][0], num)
            buckets[bucket_index][1] = max(buckets[bucket_index][1], num)
        
        # compute the maximum difference
        max_diff = 0
        prev_max = buckets[0][1]
        for i in range(1, num_buckets):
            if buckets[i][0] == float('inf'):
                continue
            max_diff = max(max_diff, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
        
        return max_diff