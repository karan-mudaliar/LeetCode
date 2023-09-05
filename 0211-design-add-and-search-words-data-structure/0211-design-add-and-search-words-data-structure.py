class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.end = True
        

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if len(word) == index:
                return node.end
            
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child,index + 1):
                        return True
            
            if word[index] in node.children:
                return dfs(node.children[word[index]],index + 1)
            
            return False
        
        return dfs(self.root,0)
        
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)