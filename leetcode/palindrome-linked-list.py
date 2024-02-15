# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 

        # Finding Midpoint 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        prev, curr = None, slow 

        # Reversing the second half 
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        
        first_half, reversed_half = head, prev 

        # Checking if it's palidrome?
        while first_half and reversed_half:
            if first_half.val != reversed_half.val:
                return False 
            
            first_half = first_half.next 
            reversed_half = reversed_half.next 
        
        return True 

        

