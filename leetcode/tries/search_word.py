class TrieNode:
    def __init__(self):
        self.child: dict = {}
        self.end: bool = False


class WordDictionary:
    """
    Tree implementation
    """

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.child.setdefault(letter, TrieNode())
        current.end = True

    def search(self, word: str, root=None) -> bool:
        current = root or self.root
        for index, letter in enumerate(word):
            if letter == ".":
                for values in current.child.values():
                    if self.search(word[index + 1:], values):
                        return True
            try:
                current = current.child[letter]
            except KeyError:
                return False
        return current.end
