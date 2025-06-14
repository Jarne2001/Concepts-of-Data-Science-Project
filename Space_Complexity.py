"""
Function to test the space complexity of the implemented Ternary Search Tree. It tests the memory usage
when inserting words into the Ternary Search Tree (the current and highest memory use).
"""

import tracemalloc

def space_complexity(word_list):
  tree = TernarySearchTree()
  if not word_list:
    raise KeyError("No word list given!")
  if len(word_list) == 0:
    raise KeyError("No words in word list!")
  tracemalloc.start()

  tree.insert(word) for word in word_list
  memory_usage = tracemalloc.get_traced_memory()
  current_memory_usage = memory_usage[0]
  highest_memory_usage = memory_usage[1]
  tracemalloc.stop()

  return current_memory_usage, highest_memory_usage
  
