class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        def get_bump(passed, students):
            top = students - passed
            bot = students * (students + 1)
            return top / bot
        
        heap = []
        for i in range(n):
            bump = get_bump(classes[i][0], classes[i][1])
            heappush(heap, (-bump, i))
        
        while extraStudents:
            bump, idx = heappop(heap)
            classes[idx][0] += 1
            classes[idx][1] += 1

            new_bump = get_bump(classes[idx][0], classes[idx][1])
            heappush(heap, (-new_bump, idx))

            extraStudents -= 1
        
        total = 0
        for passed, students in classes:
            total += passed / students
        
        return total / n
