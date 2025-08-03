from sortedcontainers import SortedList


class StockPrice:
    def __init__(self):
        self.priceInfo = {}
        self.prices = SortedList()
        self.latestTimestamp = -1

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latestTimestamp:
            self.latestTimestamp = timestamp

        if timestamp in self.priceInfo:
            old_price = self.priceInfo[timestamp]
            self.prices.remove(old_price)

        self.priceInfo[timestamp] = price
        self.prices.add(price)

    def current(self) -> int:
        return self.priceInfo[self.latestTimestamp]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]
