# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        fixed = ListNode()
        while tail.next:
            if tail.next.val >= x:
                fixed = tail
                break
            tail = tail.next
        if fixed == ListNode():
            return head
            
        prev = fixed
        curr = fixed.next
        while curr:
            if curr.val >= x:
                curr = curr.next
                prev = prev.next
            else:
                prev.next = curr.next
                nxtFixed = fixed.next
                fixed.next = curr
                curr.next = nxtFixed
                fixed = curr
                curr = prev.next
        return dummy.next


        