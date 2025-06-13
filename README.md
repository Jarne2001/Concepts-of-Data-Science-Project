# Concepts-of-Data-Science-Project
This repository is for working on the Concepts of Data Science Project. The project is an implementation of a ternary search tree with an object-oriented programming approach in Python. The implemented Ternary Search Tree has full support for word insertion, word deletion, word search, tree traversal, word checking and performance benchmarking. Additionally, a comparison is made with a Binary Search Tree and a time complexity analysis of the insert() and search() functions is performed.

# Repository content

The repository consists of the following files:

- **Binary Tree.py**: Given Binary Search Tree implementation, needed for comparison purposes.
- **Space Complexity.py**: Python function to test for the space complexity of the current Ternary Search Tree implementation.  
- **Ternary Search Tree.py**: Actual implementation of the Ternary Search Tree.  
- **corncob_lowercase.txt**: English dictionary of 50,000 lowercase words (http://www.mieliestronk.com/corncob_lowercase.txt).  
- **insert_words-checkpoint.txt**: File containing checkpoints for the insert_words.txt file.  
- **insert_words.txt**: Given test words to test the Ternary Search Tree.  
- **job script**: Job script to run benchmarking on the HPC infrastructure.  
- **not_insert_words-checkpoint.txt**: File containing checkpoints for the not_insert_words.txt file.  
- **not_insert_words.txt**: Words not inserted into the tree, used to validate negative search cases.  
- **project_2024_2025.docx**: Project description from the Concepts of Data Science course.  
- **time_complexity_discuss**: A written discussion of expected time and space complexity.  
- **time_plots.py**: Time plots showing performance metrics for the tree implementation.

# Discussion of the expected time and space complexity

In a ternary search tree, functions like search, insert, or delete on a word of length k (k characters of a string) in a tree holding n 
(n is total number of stored words) words have clearly defined performance bounds. In the best case, when the tree is perfectly balanced and each 
character comparison immediately follows the "equal" child the time complexity is O(k). In more typical conditions with randomized 
strings, the time complexity becomes O(log n+k), because a small number of left and right comparisons are made (logarithmic in the number of stored 
words) plus one middle‑child step for each character. However, in the worst case, such as when words are inserted in sorted order and the tree degenerates 
into a very long chain each tree step can take O(n+k) time, as each character search may traverse nearly all nodes before continuing to the next character 
(en.wikipedia.org).

Regarding space complexity, a ternary search tree uses one node per character of all the words it stores, and each node holds three children plus a character and 
a small flag. Thus the total space required is O(n×k), proportional to the summed length of all words the tree contains. Since this implementation uses an 
iterative approach, it is expected to go faster as well.
Summarized, a word of length k in a ternary search tree of n words, it performs in O(k) time in the best case, O(log n + k) in the average case, 
and O(n+k) in the worst case, while using O(n×k) memory.

# Conclusions



