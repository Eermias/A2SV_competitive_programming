class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChars = {
                         "2" : "abc", 
                         "3" : "def", 
                         "4" : "ghi", 
                         "5" : "jkl", 
                         "6" : "mno", 
                         "7" : "pqrs", 
                         "8" : "tuv", 
                         "9" : "wxyz"
                         }
        combinations = []
        def backtrack(i, curStr):
            if i == len(digits):
                combinations.append(curStr)
                return
            
            for c in digitsToChars[digits[i]]:
                backtrack(i + 1, curStr + c)
            
        if digits:
            backtrack(0, "")
        return combinations
        