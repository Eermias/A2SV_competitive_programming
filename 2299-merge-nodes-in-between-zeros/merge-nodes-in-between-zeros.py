# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while head:
            if head.next and head.val == 0:
                tail.next = ListNode()
                tail = tail.next
            else:
                tail.val += head.val
            head = head.next
        
        return dummy.next

