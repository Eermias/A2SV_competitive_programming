class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        count = 0
        while amount[0] and amount[1] and amount[2]:
            amount[1] -= 1
            amount[2] -= 1
            amount.sort()
            count += 1
        return count + max(amount)

        