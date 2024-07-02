class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums1:
            count[n] += 1
        
        intersection = []
        for n in nums2:
            if count[n] > 0:
                intersection.append(n)
                count[n] -= 1
        
        return intersection