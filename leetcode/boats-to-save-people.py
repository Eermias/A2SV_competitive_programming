class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        ptrLeft = 0
        ptrRight = len(people) - 1
        while ptrLeft <= ptrRight:
            if ptrLeft == ptrRight:
                count += 1
                break
            elif people[ptrLeft] + people[ptrRight] <= limit:
                count += 1
                ptrLeft += 1
                ptrRight -= 1
            else:
                count += 1
                ptrRight -= 1

        return count
        