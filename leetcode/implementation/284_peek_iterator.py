# Below is the interface for Iterator, which is already defined for you.
#
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peak = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peak > 0:
            return self.peak
        self.peak = self.iterator.next()
        return self.peak

    def next(self):
        """
        :rtype: int
        """
        if self.peak > 0:
            result = self.peak
            self.peak = 0
            return result
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peak > 0:
            return True
        return self.iterator.hasNext()
