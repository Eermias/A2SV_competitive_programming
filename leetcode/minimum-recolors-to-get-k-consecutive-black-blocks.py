class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_recolors = 0
        l = 0
        r = 0
        while r < k:
            if blocks[r] == "W":
                curr_recolors += 1
            r += 1
        #print(blocks[:r], curr_recolors)
        r -= 1
        minRecolors = curr_recolors

        while r < len(blocks):
            l += 1
            r += 1
            if r < len(blocks):
                if blocks[l - 1] == "W":
                    curr_recolors -= 1
                if blocks[r] == "W":
                    curr_recolors += 1
                minRecolors = min(minRecolors, curr_recolors)
            

        return minRecolors


        