class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        prev = timePoints[0].split(':')
        minn = float("inf")
        
        for i in range(len(timePoints)):
            if i == 0:
                curr = timePoints[-1].split(':')
            else:
                curr = timePoints[i].split(':')

            first = int(prev[0]) * 60 + int(prev[1])
            second = int(curr[0]) * 60 + int(curr[1])
            if i > 0:
                prev = curr

            diff = abs(first - second)
            if diff <= 12 * 60:
                minn = min(minn, diff)
            else:
                if first > 12 * 60:
                    first = (12 * 60) - first % (12 * 60)
                else:
                    first *= -1
                if second > 12 * 60:
                    second = (12 * 60) - second % (12 * 60)
                else:
                    second *= -1

                minn = min(minn, abs(first - second))

        return minn