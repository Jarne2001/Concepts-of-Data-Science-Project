# This Python file contains the code for the implementation of a Ternary Search Tree with an object-oriented approach.

# I suggest making 2 classes: a Ternary Search Tree Node and a Ternary Search Tree with currently 3 functions: insert, search and delete (and
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
    word = list(word)
    if self._root is None:
      self._root == insert(self.root, word[0])
      
      
      
  
