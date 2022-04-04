
#Replace Words 

# (https://leetcode.com/problems/replace-words/)



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
    
    def find_smallest_root(self, word):
        
        node = self.root
        
        output = []
        
        for char in word:
            
            if node.isChildNone(char):
                return ""
            node = node.get_child(char)
            
            output.append(char)
            if node.get_end():
                return "".join(output)
        return ""
                



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        sentence_lst = sentence.split(" ")
        output_sent = []
        for word in sentence_lst:
            root = trie.find_smallest_root(word)
            
            if root == "":
                output_sent.append(word)
            else:
                output_sent.append( root )
        return " ".join(output_sent)
            
        