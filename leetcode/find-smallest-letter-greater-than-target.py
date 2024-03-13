class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest_greater = letters[0]
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l + r) // 2
            if letters[m] > target:
                smallest_greater = letters[m]
                r = m - 1
            else:
                l = m + 1
        
        return smallest_greater
        