class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
        
        return -1
        