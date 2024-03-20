# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        plug = dummy
        tail = head
        while tail:
            start = tail
            count = k - 1
            while count and tail:
                tail = tail.next
                count -= 1
            if tail: #fully iterated
                end = tail
                tail = tail.next
                end.next = None

                prev = None
                curr = start
                while curr:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                plug.next = prev
                plug = start
            else:
                plug.next = start
         

        return dummy.next


        