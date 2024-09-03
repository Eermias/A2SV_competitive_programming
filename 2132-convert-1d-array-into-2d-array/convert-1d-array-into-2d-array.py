class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        else:
            matrix = []
            for i in range(m):
                start = n * i
                row = []
                for j in range(start, start + n):
                    row.append(original[j])
                matrix.append(row)
            
            return matrix