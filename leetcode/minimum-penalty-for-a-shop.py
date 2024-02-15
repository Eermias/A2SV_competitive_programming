class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0] #the numbers of yes's till current hour
        for i in range(len(customers)):
            if customers[i] == "Y":
                prefix.append(1)
            else:
                prefix.append(0)
            prefix[i + 1] += prefix[i]
        min_pen = float("inf")
        index = 0
        for i in range(len(prefix)):
            close_pen = prefix[-1] - prefix[i]
            open_pen = i - prefix[i]
            curr_pen = close_pen + open_pen
            if curr_pen < min_pen:
                min_pen = curr_pen
                index = i
        return index
        
             
            

        