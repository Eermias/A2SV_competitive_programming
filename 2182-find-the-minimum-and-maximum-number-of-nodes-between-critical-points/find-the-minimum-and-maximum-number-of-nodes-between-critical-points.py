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

        first, last = -1, -1
        idx = 1
        minn = float("inf")
        while _next:
            if ((curr.val > prev.val and curr.val > _next.val) or
                (curr.val < prev.val and curr.val < _next.val)):
                if first == -1:
                    first = idx
                else:
                    minn = min(minn, idx - last)
                last = idx
            prev = curr
            curr = _next
            _next = _next.next
            idx += 1
        
        if last == first:
            return [-1, -1]
        return [minn, last - first]

            