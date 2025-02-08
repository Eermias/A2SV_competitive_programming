class NumberContainers:

    def __init__(self):
        self.min_index = defaultdict(list)
        self.options = defaultdict(set)
        self.indices = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.indices:
            self.options[self.indices[index]].remove(index)
        self.indices[index] = number
        heappush(self.min_index[number], index)
        self.options[number].add(index)


    def find(self, number: int) -> int:
        while self.min_index[number] and self.min_index[number][0] not in self.options[number]:
            heappop(self.min_index[number])

        if not self.min_index[number]:
            return -1
        return self.min_index[number][0]
            
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)