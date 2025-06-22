class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.array = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        result = self.snap_id
        self.snap_id += 1
        return result

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        left, right = 0, len(history) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if history[ans][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return history[ans][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
