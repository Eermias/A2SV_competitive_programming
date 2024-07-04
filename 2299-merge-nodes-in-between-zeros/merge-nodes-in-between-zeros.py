# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        tail = head
        while tail and tail.next:
            if tail.next and tail.next.val == 0:
                prev = tail
                tail = tail.next
            elif tail.next:
                tail.val += tail.next.val
                tail.next = tail.next.next
            
        prev.next = tail.next
        return head

