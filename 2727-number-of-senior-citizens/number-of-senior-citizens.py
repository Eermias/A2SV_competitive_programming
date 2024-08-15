class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for info in details:
            if int(info[11 : 13]) > 60:
                count += 1
        return count