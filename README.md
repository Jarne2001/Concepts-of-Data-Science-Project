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

# Plots discussion

In this implementation, the best case is defined by splitting a word list with a median-approach to make the tree as perfectly balanced as possible. 
Each character node more or less splits its "less than" and "greater than" branches evenly. Searching any word of length k simply follows the middle 
links k times, giving O(k) time. The average case is defined by inserting words in a random order, so that the tree stays roughly balanced on average. 
The search function then spends a small amount of time doing binary‐search-style left/right comparisons (about O(log n) overall) before following the k 
middle links, for a total of O(log n+k). The worst case is defined by sorting the word list alphabetically, causing every new word to be placed onto one side 
of the tree, turning it into a long chain. Searching then may scan through up to n nodes at each character before continuing to the next node, so in 
the worst case there is O(n+k) time.

# Insert function performance time

![Figure 1: 3 plots representing the performance time for the insert function of the implemented ternary search tree, for different performance cases](https://raw.githubusercontent.com/Jarne2001/Concepts-of-Data-Science-Project/refs/heads/main/insert_comparison_ternary_tree.png)

When the performance time for the insert function is plotted against the number of words already in the tree, three mostly straight lines are observed, 
with one for each insertion in a case (Fig. 1). In theory, "best-case" inserts should cost O(k) time and therefore stay flat as the tree grows; "average-case" 
should cost O(log n+k), rising only very slowly (logarithmically) with n; and "worst-case" should cost O(n+k), rising in direct proportion to the tree size.
The worst-case curve behaves exactly as expected: it climbs steeply and linearly, so inserting into a degenerate, one-sided tree takes time proportional to n. 
It is also the curve that has the longest performance time as expected. The best-case curve, by contrast, does not stay perfectly flat but slopes mostly upward. 
This can be explained because always following the middle child still causes each character comparison to do left and right children checking, which becomes more 
time-expensive as the tree grows. The average-case line ends up looking almost linear too, rather than an expected logarithmic bend. That tells the "random" 
word-list insertion order did not keep the implemented tree balanced enough in practice. Each insert paid more and more left and right traversals as n grew, so 
the cost crept closer to O(n) than to O(log n). It could also be because at n = 50000 there is a very small logarithmic increase compared to n rising by 10000's, 
and this growth looks constant on a millisecond-scale Y-axis. Over the entire 50000 range is only a small increase.

In summary, the three curves do preserve the order best < average < worst, but only the worst-case truly matches its theoretical slope. This is because actual 
words and suboptimal tree balancing make even the "best" and "average" lines pick up an n-dependence and because actual code does not always fit theory.

# Search function performance time

The plot with search time against tree size in words, all three best, average and worst curves rise almost perfectly linearly, even though theory says best-case should 
be O(k) (flat) and average-case should be O(log n+k) (very slowly rising). Basically big O-notation describes asymptotic growth and hides constant factors (like
the node children checks), and not the exact shape of the practical curves which measure more than just asymptotic growth (real code also carries overheads 
and is hardware-dependent). This could also be because the average case with random inserts to not be 
perfectly randomly balanced and thus the performance approaching O(n+k) more. Also the logarithmic growth might be very small on a large plot scale like here. 
As for the best case scenario searching a character still involves the tree checking the lo and hi children with each step. As the tree grows, these nodes take 
up RAM and tree traversals become slower, still causing a linear slope as well.

In short, the theoretical k-or log-shaped curves are masked by the large scale, slightly skewed word list, lo and hi-checking and imperfect balancing, 
so all three measured search times march upward in proportion to the size of the ternary search tree.

# Comparison with B-tree

A ternary search tree stores one character per node and uses three children—low, equal, and high—making it ideal for prefix-based functions like 
autocomplete. It offers O(k) best-case time for a string of length k, O(log n+k) for the average case, but can degrade to O(k+n) in the worst case due to unbalanced insertions. 
In contrast, a B-Tree stores multiple characters per node, keeping nodes balanced and height shallow, which causes consistent O(log n) performance 
for search and insert functions in the best, worst and average case. Ternary search trees are often faster than naïve binary search trees for strings, 
due to prefix sharing and character traversal. For large string datasets, B-Trees theoretically outperform ternary search trees in performance time.

# Ternary search tree vs B-tree plots comparison

As observed on the B-tree plots for the insert and search functions, the worst case shows a linear growth an takes extremely long to run for 50000 words, 
making the other cases (which are assumed to have a logarithmic growth) appear flat because of the performance time scale difference (logarithmic growth looks constant
on linear time scale). These average and best case performances most likely are linearly increasing, similar to the ternary search tree. The 
reason why the worst case takes so long is not only because all the words are sorted, but also because the used B-tree implementation uses a recursive approach. This is
known to take longer than an iterative version.

# Conclusions

In summary, the three curves for the ternary search tree do preserve the order best < average < worst, but only the worst-case truly matches its theoretical slope. 
This is because actual words and suboptimal tree balancing make even the "best" and "average" lines pick up an n-dependence and because actual code does not always fit theory.
In short, the theoretical k-or log-shaped curves are masked by the large scale, slightly skewed word list, lo and hi-checking and imperfect balancing, 
so all three measured search times march upward in proportion to the size of the ternary search tree.

The plots show that a B-tree is overall slower in performance time, mostly dominated by the worst case, for both the insert and search functions for a large string dataset (50000 words), especially in the worst case. This goes in against the theorized faster performance time for large datasets of a B-tree, however its approach is recursive which could also increase performance time.

# References:

Bentley, J. L., & Sedgewick, R. (1997). Ternary search trees. Dr. Dobb’s Journal, 22(4), 20–26. Retrieved from https://www.drdobbs.com/database/ternary-search-trees/184410528
GeeksforGeeks (2025). Introduction of B‑tree. Retrieved June 13, 2025, from https://www.geeksforgeeks.org/introduction-of-b-tree-2/
Wikipedia contributors (2025). B‑tree. In Wikipedia, The Free Encyclopedia. Retrieved June 13, 2025, from https://en.wikipedia.org/wiki/B-tree
Wikipedia contributors (2024). Ternary search tree. In Wikipedia, The Free Encyclopedia. Retrieved June 11, 2025, from https://en.wikipedia.org/wiki/Ternary_search_tree
