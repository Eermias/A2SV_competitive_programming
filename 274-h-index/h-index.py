class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        citations.sort()

        max_index = 0
        for i in range(n):
            index = min(citations[i], n - i)
            max_index = max(index, max_index)
        
        return max_index



        