# This Python file contains the code for the implementation of a Ternary Search Tree with an object-oriented approach.

# I suggest making 2 classes: a Ternary Search Tree Node and a Ternary Search Tree with currently 4 functions: insert, search, all_strings and delete (and
# potentially also a function printing out the tree?)

class TernarySearchTreeNode:
  def __init__(self, letter):
    self.letter = letter
    self.lo, self.equal, self.hi, self.word_end = None

class TernarySearchTree:
  def __init__(self):
    self._root = None
    self._string_list = []

  def insert(self, word):
    if not word:
      raise KeyError("No word is given!")
    index = 0
    self._string_list.append(word)
    if self._root is None:
      self._root = TernarySearchTreeNode(word[index])
    node = self._root
    while index < len(word):
      letter = word[index]
      if letter > node.letter:
        if node.hi is None:
          node.hi = TernarySearchTreeNode(letter)
        node = node.hi
        continue
      if letter < node.letter:
        if node.lo is None:
          node.lo = TernarySearchTreeNode(letter)
        node = node.lo
        continue
      elif letter == node.letter:
        index += 1
        if index == len(word):
          node.end_word = True
          return
        if node.equal == None:
          node.equal = TernarySearchTreeNode(word[index])
        node = node.equal

  def all_strings(self):
    if not self._string_list:
      print("Tree is empty!")
      return []
    return set(self._string_list)
  
  def search(self, word):
    if not word:
      raise KeyError("No word is given!")
    if self._root is None:
      return False
    node = self._root
    if node.letter != word[0]:
      return False
    index = 1
    node = node.equal
    
    while len(word) > index:
      letter = word[index]
      if letter > node.letter:
        node = node.hi
        continue
      if letter < node.letter:
        node = node.lo
        continue
      if letter == node.letter:
        node = node.equal
        index += 1
        continue
      else:
        return False
    node.word_end = True
    return True

  def len(self):
    if not self._string_list:
      return 0
    return len(self._string_list)
    
  def delete(self, word):
    """
   wat er moet gebeuren is, als het de laatste letter is van het ene woord, dat moet wordenv verwijderd, dan moet alles alle letters worden verwijderd 
   totdat er een aftakking is of de volgende woord eindigd 
    """
    if word not in self._string_list:
      raise KeyError(f"{word} is not in the tree.")
    elif not word:
      raise KeyError("No word is given!")
    index = 0
    self._string_list.remove(word)
    path = []
    node = self._root
    while index < len(word):
      letter = word[index]
      if letter > node.letter:
        path.append((node, 'hi'))
        node = node.hi
        continue
      elif letter < node.letter:
        path.append((node, 'lo'))
        node = node.lo
        continue
      else:
        path.append((node, 'equal'))
  
        if index == len(word) - 1:
          node.word_end = False
          break
        
        node = node.equal
        index += 1
        
    while path and not node.lo and not node.hi and not node.equal and not node.word_end:
      i, j = path.pop()
      if j == 'lo':
        i.lo = None
      elif j == 'hi':
        i.hi = None
      else:
        i.equal = None
    node = i
    return True

  def print(self, print):
    """
    Here comes the print function, textual or visual, which should first display the root, and each time check whether the node has multiple children or one, these should be displayed in the row.
    For each layer, it should be checked each time how many letters it contains.
    """
  
      
      
  
