class NumberContainers:

    def __init__(self):
        self.nums = defaultdict(list)
        self.indices = defaultdict(int)
        

    def change(self, index: int, number: int) -> None:
        self.indices[index] = number
        heappush(self.nums[number], index)

    def find(self, number: int) -> int:
        while self.nums[number]:
            if self.indices[ self.nums[number][0]] != number:
                heappop(self.nums[number])
            else:
                return self.nums[number][0]
        
        return -1
    
            
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)