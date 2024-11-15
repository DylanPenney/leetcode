# Time Complexity: O(n)
# Space Complexity: O(t)
class TrieNode:

    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.EOW = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False

            curr=curr.children[letter]

        return curr.EOW

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False
            
            curr=curr.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)