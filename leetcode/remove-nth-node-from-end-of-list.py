# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start = dummy
        end = head
        for i in range(n):
            end = end.next
        while end:
            start = start.next
            end = end.next
        start.next = start.next.next
        return dummy.next
        