# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy 

        ptr1 = list1
        ptr2 = list2
        while ptr1 != None and ptr2 != None: 
            if ptr1.val <= ptr2.val:
                dummy.next = ptr1
                dummy = dummy.next
                ptr1 = ptr1.next
            else:
                dummy.next = ptr2
                dummy = dummy.next
                ptr2 = ptr2.next
                
        if ptr1 != None:
            dummy.next = ptr1
        if ptr2 != None:
            dummy.next = ptr2

        return head.next