# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tailA = headA
        tailB = headB
        countA, countB = 0, 0
        while tailA:
            countA += 1
            tailA = tailA.next
        while tailB:
            countB += 1
            tailB = tailB.next
        diff = countA - countB
        startA = headA
        startB = headB

        if diff > 0:
            for i in range(diff):
                startA = startA.next
        elif diff < 0:
            for i in range(abs(diff)):
                startB = startB.next
        #basecase
        if startA == startB:
            return startA
        while startA.next and startB.next:
            if startA.next == startB.next:
                return startA.next
            startA = startA.next
            startB = startB.next
        return None
        