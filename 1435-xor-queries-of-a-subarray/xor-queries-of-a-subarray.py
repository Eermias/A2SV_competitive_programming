class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr = [0] + arr
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
        answer = []
        for l, r in queries:
            xor = arr[r + 1] ^ arr[l]
            answer.append(xor)
        
        return answer
