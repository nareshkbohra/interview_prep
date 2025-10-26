class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for b_start, b_end in self.bookings:
            if startTime < b_end and endTime > b_start:
                return False

        self.bookings.append((startTime, endTime))
        return True
