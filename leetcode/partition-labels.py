class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        allMap ={} #char : lastIndex
        res = []
        for i in range(len(s)):
            allMap[s[i]] = i
        j = 0
        while j < len(s):
            char = s[j]
            last = allMap[char]
            #print(j, char, last)
            start = j
            cut = last
            for k in range(start, last):
                cut = max(cut, allMap[s[k]])
                if k == last - 1:
                    while last < cut:
                        cut = max(cut, allMap[s[last]])
                        last += 1
            res.append(cut - start + 1)
            j = cut + 1
        return res


        