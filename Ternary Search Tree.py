# This Python file contains the code for the implementation of a Ternary Search Tree with an object-oriented approach.

# I suggest making 2 classes: a Ternary Search Tree Node and a Ternary Search Tree with currently 4 functions: insert, search, all_strings and delete (and
# potentially also a function printing out the tree?)

class(TernarySearchTreeNode):
  def __init__(self, letter):
    self.letter = letter
    self.lo, self.equal, self.hi = None

class (TernarySearchTree):
  def __init__(self):
    self._root = None

  def insert(self, word):
    if not word:
      raise KeyError("No word is given!")
    index = 0
    node = None
    string_list = []
    string_list.append(word)
    if self._root is None:
      self._root == self.insert(self.root, word[index])
      return
    else:
      letter = word[index]
      if node == None:
        node = TernarySearchTreeNode(letter)
      while index < len(word):
        if letter > node.letter:
          if node.hi is None:
            node.hi = self.insert(node.hi, letter)
            index += 1
        if letter < node.letter:
          if node.lo is None:
            node.lo = self.insert(node.lo, letter)
            index += 1
        if letter == node.letter:
          if node.equal is None:
            node.equal = self.insert(node.equal, letter)
            index += 1
        if index == len(word):
          return node

  def all_strings(self):
    if not string_list:
      return print("Tree is empty!")
    return string_list

  def len(self):
    if not string_list:
      return 0
    return len(string_list)
    
    
      
      
      
  
