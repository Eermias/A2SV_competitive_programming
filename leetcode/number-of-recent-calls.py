class RecentCounter:

    def __init__(self):
        self.request = [[0, 0]]
        self.start = 0
        

    def ping(self, t: int) -> int:
        self.request.append([t, 1 + self.request[-1][1]])
        while self.request[-1][0] - self.request[self.start][0] > 3000:
            self.start += 1
        #if self.request[self.start] == self.request[-1]:
           # self.start -= 1
        return self.request[-1][1] - self.request[self.start - 1][1] if self.start > 0 else self.request[-1][1]
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)