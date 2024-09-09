class Solution:

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        # Step 1: Find the minimum and maximum values
        min_val, max_val = min(nums), max(nums)
        n = len(nums)

        # Step 2: Compute the minimum possible maximum gap
        gap = math.ceil((max_val - min_val) / (n - 1))
        if gap == 0:
            return 0  # All numbers are the same

        # Step 3: Initialize buckets
        buckets_min = [float('inf')] * (n - 1)
        buckets_max = [float('-inf')] * (n - 1)

        # Step 4: Populate the buckets
        for num in nums:
            if num == min_val or num == max_val:
                continue  # Skip min and max
            idx = (num - min_val) // gap
            buckets_min[idx] = min(num, buckets_min[idx])
            buckets_max[idx] = max(num, buckets_max[idx])

        # Step 5: Calculate the maximum gap
        max_gap = 0
        prev = min_val

        for i in range(n - 1):
            if buckets_min[i] == float('inf') and buckets_max[i] == float('-inf'):
                continue  # Skip empty buckets

            # Calculate gap between buckets
            max_gap = max(max_gap, buckets_min[i] - prev)
            prev = buckets_max[i]

        # Compare with the maximum value
        max_gap = max(max_gap, max_val - prev)

        return max_gap

