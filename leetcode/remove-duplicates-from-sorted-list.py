# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = head
        while tail and tail.next:
            while tail.next and tail.val == tail.next.val:
                tail.next = tail.next.next
            tail = tail.next
        return head
        