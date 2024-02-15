class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ptr = 0
        prefix = nums[0]
        count = 0
        if nums[0] != 1:
            prefix = 0
            num = 1
            while prefix < nums[0] - 1:
                prefix += num
                count += 1
                num = prefix + 1
            prefix += nums[0]
            print(prefix, count)
        i = 1
        while i < n + 1:
            if i > prefix:
                if ptr == len(nums) - 1 or nums[ptr + 1] > i:
                    prefix += i
                    count += 1
                else:
                    ptr += 1
                    prefix += nums[ptr]
            else:
                i = prefix + 1

        return count
        