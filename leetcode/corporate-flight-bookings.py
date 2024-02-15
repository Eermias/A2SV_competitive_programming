class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n + 1)
        for booking in bookings:
            flights[booking[0]] += booking[2]
            if booking[1] + 1 < n + 1:
                flights[booking[1] + 1] -= booking[2]
        for i in range(1, len(flights)):
            flights[i] += flights[i - 1]
        return flights[1:]
        