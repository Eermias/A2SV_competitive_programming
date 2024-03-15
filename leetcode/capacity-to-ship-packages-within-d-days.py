class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), 500 * 5 * 10**4
        min_capacity = high
        while low <= high:
            capacity = (low + high) // 2
            time = 0
            load = 0
            """for weight in weights:
                load += weight
                if load > capacity:
                    time += 1
                    load = weight"""
            for i in range(len(weights)):
                load += weights[i]
                if load > capacity:
                    time += 1
                    load = weights[i]
                if i == len(weights) - 1 and load:
                    time += 1
            if time <= days:
                min_capacity = min(min_capacity, capacity)
                high = capacity - 1
            else:
                low = capacity + 1
        
        return min_capacity



                
