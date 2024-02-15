# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = head.next
        while odd and even and even.next:
            temp1 = odd.next
            temp2 = even.next.next
            odd.next = even.next
            odd = odd.next
            odd.next = temp1
            even.next = temp2
            even = even.next
        return head

        