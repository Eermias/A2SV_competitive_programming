class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        t = 0
        f = 0
        start = 0
        end = 0
        maximum = 0
        while end < len(answerKey):
            if t>k and f>k:
                if answerKey[start] == 'T':
                    t -= 1
                else:
                    f -= 1
                start += 1
            else:
                if answerKey[end] == 'T':
                    t += 1
                else:
                    f += 1

                if not(f>k and t>k):
                    maximum = max(maximum, end-start+1)
                end += 1
        return maximum
    
