class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        q=deque([i for i in range(len(tickets))])
        
        time=0
        
        while q:
            for i in range(len(q)):

                node=q.popleft()
                tickets[node]-=1
                if tickets[node]>=1:
                    q.append(node)
                
                time+=1
                if tickets[k]==0:
                    return time
            
        