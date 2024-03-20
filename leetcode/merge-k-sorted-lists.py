# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        ptr1, ptr2 = list1, list2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next
        if ptr1:
            tail.next = ptr1
        else:
            tail.next = ptr2
        
        return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        res = []
        while len(lists) != 1:
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.merge(list1, list2)
                res.append(merged)
            lists = res[:]
            res = []
        
        return lists[0]

    