# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        if not curr:
            return [-1, -1]
        _next = curr.next 

        criticals = []
        idx = 1
        minn = float("inf")
        while _next:
            if ((curr.val > prev.val and curr.val > _next.val) or
                (curr.val < prev.val and curr.val < _next.val)):
                if criticals:
                    minn = min(minn, idx - criticals[-1])
                criticals.append(idx)
            prev = curr
            curr = _next
            _next = _next.next
            idx += 1
        
        if len(criticals) < 2:
            return [-1, -1]
        return [minn, criticals[-1] - criticals[0]]

            