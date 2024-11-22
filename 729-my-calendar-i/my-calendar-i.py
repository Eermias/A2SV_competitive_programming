class MyCalendar:

    def __init__(self):
        self.booked_events = []

    def book(self, startTime: int, endTime: int) -> bool:
        okay = True
        for start, end in self.booked_events:
            left = max(start, startTime)
            right = min(end, endTime)
            if left < right:
                okay = False
                break
        
        if okay:
            self.booked_events.append([startTime, endTime])
            return True
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)