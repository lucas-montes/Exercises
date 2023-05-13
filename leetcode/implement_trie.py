from bisect import bisect_left, insort


class Trie:
    """
    The fastest and more efficient one but isn't using trees that is the
    expected solution
    """

    def __init__(self):
        self.words = set()
        self.sorted_words = list()

    def insert(self, word: str) -> None:
        self.words.add(word)
        insort(self.sorted_words, word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        index = bisect_left(self.sorted_words, prefix)
        if index == len(self.sorted_words):
            return False
        return self.sorted_words[index].startswith(prefix)


class TrieNode:
    def __init__(self):
        self.child: dict = {}
        self.end: bool = False


class Trie:
    """
    Tree implementation
    """

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.child.setdefault(letter, TrieNode())
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            try:
                current = current.child[letter]
            except KeyError:
                return False
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            try:
                current = current.child[letter]
            except KeyError:
                return False
        return True
