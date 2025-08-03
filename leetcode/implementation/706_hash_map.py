class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashMap:
    def __init__(self):
        """
        Maintain N bucket where N is prime
        """
        self.modulo = 4093
        self.buckets = [[] for _ in range(self.modulo)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.modulo
        bucket_list = self.buckets[hash_key]
        for node in bucket_list:
            if node.key == key:
                node.value = value
                break
        else:
            bucket_list.append(Node(key, value))

    def get(self, key: int) -> int:
        hash_key = key % self.modulo
        bucket_list = self.buckets[hash_key]
        for node in bucket_list:
            if node.key == key:
                return node.value
        return -1

    def remove(self, key: int) -> None:
        index = -1
        hash_key = key % self.modulo
        bucket_list = self.buckets[hash_key]
        for i, node in enumerate(bucket_list):
            if node.key == key:
                index = i
                break
        if index != -1:
            bucket_list.pop(index)
