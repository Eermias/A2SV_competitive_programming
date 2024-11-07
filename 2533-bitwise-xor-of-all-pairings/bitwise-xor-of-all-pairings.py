class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        all_xor = 0
        if len(nums1) % 2:
            for num in nums2:
                all_xor ^= num
        
        if len(nums2) % 2:
            for num in nums1:
                all_xor ^= num
        
        return all_xor