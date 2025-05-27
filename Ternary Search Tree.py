# This Python file contains the code for the implementation of a Ternary Search Tree with an object-oriented approach.

class TernarySearchTreeNode:
  """
  Node used within a Ternary Search Tree, holding one character and up to three child nodes.
  """
  def __init__(self, letter):
    self.letter = letter
    self.lo = None
    self.equal = None  
    self.hi = None
    self.word_end = False

class TernarySearchTree:
  """
  Ternary Search Tree with support for inserting, searching, deleting, printing, 
  and listing all stored strings.
  """
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
      if node is None:
        return
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
          node.word_end = True
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
    index = 0
    
    while len(word) > index:
      if node is None:
        return False
      letter = word[index]
      if letter > node.letter:
        node = node.hi
        continue
      if letter < node.letter:
        node = node.lo
        continue
      if letter == node.letter:
        index += 1
        if index == len(word):
          if node.word_end == False:
            return False
          else:
            return True
        node = node.equal
        continue
      else:
        return False
    return True

  def len(self):
    if not self._string_list:
      return 0
    return len(self._string_list)
    
  def delete(self, word):
    if word not in self._string_list:
      raise KeyError(f"{word} is not in the tree.")
    elif not word:
      raise KeyError("No word is given!")
    index = 0
    self._string_list.remove(word)
    path = []
    node = self._root
    while index < len(word):
      if node is None:
        return False
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

  def print_tst(self, print_tst):
    """
    Here comes the print function, textual or visual, which should first display the root, and each time check whether the node has multiple children or one, these should be displayed in the row.
    For each layer, it should be checked each time how many letters it contains.
    """


tst = TernarySearchTree()
words = ["combine", "combinations", "combination", "combined", "combines","ducks", "ducked", "duck","futile", "futility", "future",
         "fontain", "font","far", "a", "the", "their", "therefor", "there","bomb"]
words_2 = ["combine", "combinations", "combination", "combined", "combines","ducks", "ducked", "duck","futile", "futility", "future",
         "fontain", "font","far", "a", "the", "their", "therefor", "there","bomb", "cheese", "droog", "comb", "ine", "fut"]

for word in words:
    tst.insert(word)

print(f"Length: {tst.len()}")
print(f"All strings: {sorted(tst.all_strings())}")

for word in words_2:
    print(f"Search '{word}': {tst.search(word)}")
