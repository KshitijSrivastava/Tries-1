
# Longest Word in Dictionary
#(https://leetcode.com/problems/longest-word-in-dictionary/)


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
    
    def made_of_words(self, word):
        node = self.root
        
        for char in word:
            
            if node.isChildNone(char):
                return False
            node = node.get_child(char)
            
            if node.get_end() == False:
                return False
            #print(char)
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        output = {}
        max_length = 0
        
        for word in words:
            
            if trie.made_of_words(word):
                max_length = max(max_length, len(word))
                if len(word) not in output:
                    output[ len(word) ] = []
                output[ len(word) ].append( word )
        
        if max_length == 0:
            return ""
        output[max_length].sort( )
        return output[max_length][0]
        
            
        