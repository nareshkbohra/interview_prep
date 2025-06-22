from random import randint


class RandomizedSet:
    def __init__(self):
        self.array = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        currIndex = self.map[val]
        del self.map[val]

        if currIndex == len(self.array) - 1:
            self.array.pop()
            return True

        lastValue = self.array[-1]
        self.array[currIndex] = lastValue
        self.map[lastValue] = currIndex
        self.array.pop()

        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.array) - 1)
        return self.array[index]
