class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        last_occ = {}
        minn = len(cards)
        present = False
        for i in range(len(cards)):
            if cards[i] in last_occ:
                minn = min(minn, i - last_occ[cards[i]] + 1)
                present = True
            last_occ[cards[i]] = i
        return minn if present == True else -1
            

        
        