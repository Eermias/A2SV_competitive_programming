# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        index = 1
        while index != left:
            tail = tail.next
            index += 1
        
        #break link : left
        breakL = tail
        tail = tail.next
        breakL.next = None
        
        start = tail
        #break link : right
        while tail and index != right:
            tail = tail.next
            index += 1
        end = tail
        tail = tail.next
        end.next = None

        #reverse the broken part
        prev = None
        curr = start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #connect
        breakL.next = end
        start.next = tail
        return dummy.next



        