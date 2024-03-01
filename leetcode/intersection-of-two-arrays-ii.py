class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        for n in nums1:
            count1[n] = 1 + count1.get(n, 0)
        common = {}
        for n in nums2:
            if n in count1:
                common[n] = 1 + common.get(n, 0)
        for key in common:
            common[key] = min(common[key], count1[key])
        res = []
        for key in common:
            dup = [key] * common[key]
            res += dup

        return res