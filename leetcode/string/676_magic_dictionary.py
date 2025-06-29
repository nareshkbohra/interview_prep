from typing import List
from collections import defaultdict


class MagicDictionary:
    def __init__(self):
        self.words = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.words[(word[:i], word[i + 1 :])].append(word[i])

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            key = (searchWord[:i], searchWord[i + 1 :])
            if key in self.words:
                charList = self.words[key]
                if len(charList) > 1 or charList[0] != searchWord[i]:
                    return True
        return False
