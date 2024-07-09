class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        next_free = 0
        for arrival, prep in customers:
            if next_free > arrival:
                total += next_free - arrival + prep
                next_free += prep
            else:
                total += prep
                next_free = arrival + prep

        return total / len(customers)
