class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        count = [0] * 32
        for num in nums1:
            for i in range(32):
                if num & (1 << i):
                    count[i] += 1
        
        n = len(nums1)
        all_xor = 0
        for num in nums2:
            temp = 0
            for i in range(32):
                bit = 1 if (num & (1 << i)) else 0
                bit *= n
                bit = abs(bit - count[i])

                if bit % 2:
                    temp |= (1 << i)
            
            all_xor ^= temp
        
        return all_xor