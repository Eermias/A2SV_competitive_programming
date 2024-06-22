class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        starts = deque([[-1, 0]]) #[index, prefix]
        prefix = 0
        shortest = float("inf")
        for i, n in enumerate(nums):
            prefix += n
            while starts and prefix - starts[0][1] >= k:
                shortest = min(shortest, i - starts[0][0])
                starts.popleft()
            while starts and prefix < starts[-1][1]:
                starts.pop()
            starts.append([i, prefix])

        if shortest == float("inf"):
            shortest = -1
        return shortest

