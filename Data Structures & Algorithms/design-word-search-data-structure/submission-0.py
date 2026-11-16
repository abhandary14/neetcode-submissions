
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        # Insert each character into the Trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        # Mark the end of a complete word
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            # Match characters starting from index i
            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    # Wildcard: try every possible child
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    # Follow the matching character if it exists
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            # A valid match must end at a complete word
            return curr.endOfWord

        return dfs(0, self.root)