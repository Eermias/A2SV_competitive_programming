class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        path = []
        def backtrack(i):
            if len(path) == k:
                ans.append(path[:])
                return
            if i > n:
                return 

            # include the current in path
            path.append(i)
            backtrack(i + 1)

            # not include the current element
            path.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return ans
