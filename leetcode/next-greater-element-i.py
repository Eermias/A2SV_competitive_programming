class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st = []
        hashmap = {}
        res = [0]*len(nums1)

        # O(nums1.length)
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
        j = len(nums2) - 1
        while j >= 0:
            if nums2[j] in hashmap:
                if st == []:
                    res[hashmap[nums2[j]]] = -1
                elif st != [] and st[-1] > nums2[j]:
                    res[hashmap[nums2[j]]] = st[-1]
                elif st != [] and st[-1] <= nums2[j]:
                    while st and st[-1] <= nums2[j]:
                        st.pop()
                    if st == []:
                        res[hashmap[nums2[j]]] = -1
                    else:
                        res[hashmap[nums2[j]]] = st[-1]
            st.append(nums2[j])
            j -= 1
        return res

        
                
        