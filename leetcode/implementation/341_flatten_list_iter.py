class NestedIterator:
    def __init__(self, nestedList: ["NestedInteger"]):
        self.ni = None
        self.nestedList = nestedList
        self.i = -1

    def next(self) -> int:
        if self.ni:
            return self.ni.next()

        return self.nestedList[self.i].getInteger()

    def hasNext(self) -> bool:
        if self.ni:
            if self.ni.hasNext():
                return True
            self.ni = None
        self.i += 1
        if self.i == len(self.nestedList):
            return False

        currItem = self.nestedList[self.i]
        if currItem.isInteger():
            return True

        self.ni = NestedIterator(currItem.getList())
        return self.ni.hasNext()
