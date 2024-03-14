class TimeMap:

    def __init__(self):
        self.store = {} #key : list of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or self.store[key][0][1] > timestamp:
            return ""
        values = self.store.get(key)
        l, r = 0, len(values) - 1
        index = 0
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                #index = max(index, l)
                r = m - 1
            else:
                index = max(index, m)
                l = m + 1

        return values[index][0] 

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)