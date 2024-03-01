class Solution:
    def sortSentence(self, s: str) -> str:
        split = s.split()
        original = [""] * len(split)
        for word in split:
            originalPos = int(word[-1])
            original[originalPos - 1] = word[:-1]
        
        return " ".join(original)
        
        