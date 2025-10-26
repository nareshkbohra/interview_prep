class MyCalendarTwo:
    def __init__(self):
        self.single_booking = []
        self.double_booking = []

    def book(self, startTime: int, endTime: int) -> bool:
        for i, j in self.double_booking:
            if startTime < j and endTime > i:
                return False
        for i, j in self.single_booking:
            if startTime < j and endTime > i:
                self.double_booking.append((max(startTime, i), min(endTime, j)))
        self.single_booking.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
