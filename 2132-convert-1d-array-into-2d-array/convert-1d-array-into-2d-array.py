class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        else:
            matrix = []
            for i in range(m):
                start = n * i
                row = original[start : start + n]
                matrix.append(row)
            
            return matrix