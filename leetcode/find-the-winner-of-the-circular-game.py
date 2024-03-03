class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        que = deque([i for i in range(1, n + 1)])
        temp = 1
        while que:
            node = que.popleft()
            if temp < k:
                que.append(node)
                temp += 1
            else:
                temp = 1
        return node
            

        
        