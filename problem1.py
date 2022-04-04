
#Implement Trie (Prefix Tree)(https://leetcode.com/problems/implement-trie-prefix-tree/)


class Node:
    def __init__(self):
        self.child = [None for i in range(26)]
        self.end = False
        
    def set_end(self):
        self.end = True
        
    def get_end(self):
        return self.end
        
    def index_from_char(self, char):
        return ord(char) - ord("a")
    
    def isChildNone(self, char):
        index = self.index_from_char(char)
        return self.child[index] == None
    
    def insert_char(self, char):
        index = self.index_from_char(char)
        
        if self.isChildNone(char):
            self.child[index] = Node()
        return self.child[index]
    
    def get_child(self, char):
        index = self.index_from_char(char)
        return self.child[index]
        
        

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        
        node = self.root
        
        for char in word:
            node = node.insert_char(char)
        node.set_end()
        return
        

    def search(self, word: str) -> bool:
        
        node = self.root
        
        for char in word:
            
            if node.isChildNone(char):
                return False
            node = node.get_child(char)
            
        if node.get_end():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        
        for char in prefix:
            
            if node.isChildNone(char):
                return False
            node = node.get_child(char)
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)