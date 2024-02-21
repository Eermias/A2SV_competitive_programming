class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = deque()
        while deck:
            res.appendleft(deck.pop())
            if deck:
                res.appendleft(res.pop())
        return res

        