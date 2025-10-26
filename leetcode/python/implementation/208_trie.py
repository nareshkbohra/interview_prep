class Trie:
    def __init__(self):
        self.map = {}

    def insert(self, word: str) -> None:
        if not word:
            self.map["/"] = Trie()
            return

        firstChar = word[0]
        if firstChar not in self.map:
            self.map[firstChar] = Trie()
        self.map[firstChar].insert(word[1:])

    def search(self, word: str) -> bool:
        word = word + "/"
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        firstChar = prefix[0]
        if firstChar not in self.map:
            return False
        return self.map[firstChar].startsWith(prefix[1:])

    def __repr__(self):
        return f"{self.map}"


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
t = Trie()
t.insert("naresh")
print(t.search("naressh"))
