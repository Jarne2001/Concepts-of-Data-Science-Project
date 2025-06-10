# This Python file contains the code for the implementation of a Ternary Search Tree with an object-oriented approach.
import time
import matplotlib.pyplot as plt

class TernarySearchTreeNode:
  """
  Node used within a Ternary Search Tree, holding one character and up to three child nodes.
  lo = the subtree which holds characters less than this node's characters
  equal = the subtree has equal characters
  hi = the subtree of characters which are greater than the character of this node
  """
  def __init__(self, letter):
    self.letter = letter # stored character in node
    self.lo = None
    self.equal = None  
    self.hi = None
    self.word_end = False

class TernarySearchTree:
  """
  Ternary Search Tree with support for inserting, searching, deleting, printing, 
  and listing all stored strings and the count of stored nodes.
  """
  def __init__(self):
    self._root = None # root node
    self._string_list = []

  def insert(self, word):
    """
    This function inserts a word into the tree.
    """
    if not word:
      raise KeyError("No word is given!") # if no word is given
    index = 0
    self._string_list.append(word) # keeps a list for word retrieval
    if self._root is None: # if root is empty, initialize
      self._root = TernarySearchTreeNode(word[index])
    node = self._root
    
    while index < len(word): # traverse the tree according to each character within word
      if node is None:
        return
      letter = word[index]
      if letter > node.letter: # moves to right subtree
        if node.hi is None:
          node.hi = TernarySearchTreeNode(letter)
        node = node.hi
        continue
      if letter < node.letter: # move to left subtree
        if node.lo is None:
          node.lo = TernarySearchTreeNode(letter)
        node = node.lo
        continue
        
      elif letter == node.letter: # when character matches
        index += 1
        if index == len(word):
          node.word_end = True
          return
        if node.equal == None:
          node.equal = TernarySearchTreeNode(word[index])
        node = node.equal

  def all_strings(self):
    """
    This function returns all inserted words into the tree.
    """
    if not self._string_list:
      print("Tree is empty!") # if no words in tree
      return []
    return set(self._string_list)
  
  def search(self, word):
    """
    This function searches a full word in the tree. It returns True when
    the tree contains the word, otherwise False.
    """
    if not word:
      raise KeyError("No word is given!") # if no word is specified
    if self._root is None:
      return False
    node = self._root
    index = 0
    
    while len(word) > index: # traverse each character in word
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
    """
    This function returns the number of words inside the tree
    """
    if not self._string_list:
      return 0
    return len(self._string_list)
    
  def delete(self, word):
    """
    This function deletes a word from the tree
    """
    if word not in self._string_list:
      raise KeyError(f"{word} is not in the tree.") # if word not present
    elif not word:
      raise KeyError("No word is given!") # if no word is given
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
        
    while path and not node.lo and not node.hi and not node.equal and not node.word_end: # type: ignore
      i, j = path.pop()
      if j == 'lo':
          i.lo = None
      elif j == 'hi':
          i.hi = None
      else:
          i.equal = None
      node = i
    return True

  def print_tst(self):
    """
    This function prints the current Ternary Search Tree, with the root and characters 
    per word
    """
    if not self._string_list:
      print("Tree is empty!")
      return
    print(f"terminates: {self._root.word_end}")
    print(f"       char: {self._root.letter}, terminates: {self._root.word_end}") # prints the root details
    nodes_to_print = []
    spaces = "  " 
    if self._root.equal:
        nodes_to_print.append((self._root.equal, "_eq:", ""))
    if self._root.lo:
        nodes_to_print.append((self._root.lo, "_lo:", ""))
    if self._root.hi:
        nodes_to_print.append((self._root.hi, "_hi:", ""))

    while len(nodes_to_print): # traverses the ternary search tree
        node_now, direction, current_spaces = nodes_to_print.pop(0)
        print(f"{direction}{current_spaces}      char: {node_now.letter}, terminates: {node_now.word_end}")
        new_spaces = current_spaces + "  "
        if node_now.hi:
            nodes_to_print.append((node_now.hi, "_hi:", new_spaces))
        if node_now.lo:
            nodes_to_print.append((node_now.lo, "_lo:", new_spaces))
        if node_now.equal:
            nodes_to_print.append((node_now.equal, "_eq:", new_spaces))

def main():
  """
  This function allows to load in a word list into the main Ternary Search Tree
  function for benchmarking
  """
    # Load file
    with open('corncob_lowercase.txt', 'r') as file:
        words = [line.strip() for line in file]

    print(f"Loaded {len(words)} words")
    
    samples = [words[:100], words[:500], words[:1000], words[:2000], words[:5000]]
    
    # Test 1: Insert performance
    nr_runs = 10
    times = {}
    insert_sample = words[:20]
    
    for sample in samples:
        tst = TernarySearchTree()
        for word in sample:
            tst.insert(word)
        times[len(sample)] = 0.0
        
        for _ in range(nr_runs):
            start_time = time.time_ns()
            for word in insert_sample:
                tst.insert(word)
            end_time = time.time_ns()
            times[len(sample)] += end_time - start_time
        times[len(sample)] /= nr_runs * 1_000_000.0
    
    print(f"Insert times: {times}")     
    plt.figure()
    plt.plot(times.keys(), times.values())
    plt.title("Insert Performance")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.savefig('insert_performance.png')
    
    # Test 2: Search performance
    times = {}
    search_sample = words[:20]
    
    for sample in samples:
        tst = TernarySearchTree()
        for word in sample:
            tst.insert(word)
        times[len(sample)] = 0.0
        
        for _ in range(nr_runs):
            start_time = time.time_ns()
            for word in search_sample:
                tst.search(word)
            end_time = time.time_ns()
            times[len(sample)] += end_time - start_time
        times[len(sample)] /= nr_runs * 1_000_000.0
      
    print(f"Search times: {times}")
    plt.figure()
    plt.plot(times.keys(), times.values())
    plt.title("Search Performance")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.savefig('search_performance.png')
    print("Search done")
  
if __name__ == "__main__":
    main()
