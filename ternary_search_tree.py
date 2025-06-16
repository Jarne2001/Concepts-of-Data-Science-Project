"""
This Python file contains the code for the implementation of a Ternary Search Tree with an object-oriented approach. It contains functions to insert words, 
return all strings stored, search presence of strings, returns the tree length, deleting specific words and console-printing the tree. Additionally, it allows
to test a dataset of 500000 strings (benchmarking).
"""

import time
import random
import matplotlib.pyplot as plt


class TernarySearchTreeNode:
    """
    Node used within a Ternary Search Tree, holding one character and up to three child nodes.
    lo = the subtree which holds characters less than this node's characters.
    equal = the subtree has equal characters.
    hi = the subtree of characters which are greater than the character of this node.
    """

    def __init__(self, letter):
        self.letter = letter  # stored character in node
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
        self._root = None  # root node
        self._string_list = []

    def insert(self, word):
        """
        This function inserts a word into the tree.
        """
        if not word:
            raise ValueError("Empty string cannot be given!")  # if no word is given
        if not isinstance(word, str):
            raise TypeError("Only words of the string instance are allowed!")
        word = word.lower()
        index = 0
        self._string_list.append(word)  # keeps a list for word retrieval
        if self._root is None:  # if root is empty, initialize
            self._root = TernarySearchTreeNode(word[index])
        node = self._root

        while index < len(
            word
        ):  # traverse the tree according to each character within word
            if node is None:
                return
            letter = word[index]
            if letter > node.letter:  # moves to right subtree
                if node.hi is None:
                    node.hi = TernarySearchTreeNode(letter)
                node = node.hi
                continue
            if letter < node.letter:  # move to left subtree
                if node.lo is None:
                    node.lo = TernarySearchTreeNode(letter)
                node = node.lo
                continue

            elif letter == node.letter:  # when character matches
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
            print("Tree is empty!")  # if no words in tree
            return []
        return set(self._string_list)

    def search(self, word):
        """
        This function searches a full word in the tree. It returns True when
        the tree contains the word, otherwise False.
        """
        if not word:
            raise KeyError("No word is given!")  # if no word is specified
        if self._root is None:
            return False
        node = self._root
        index = 0

        while len(word) > index:  # traverse each character in word
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
        This function returns the number of words inside the tree (the length of the string_list).
        """
        if not self._string_list:
            return 0
        return len(self._string_list)

    def delete(self, word):
        """
        This function deletes a word from the tree if it is present.
        """
        if word not in self._string_list:
            raise KeyError(f"{word} is not in the tree.")  # if word not present
        elif not word:
            raise KeyError("No word is given!")  # if no word is given
        index = 0
        self._string_list.remove(word)
        path = []
        node = self._root

        while index < len(word):
            if node is None:
                return False
            letter = word[index]
            if letter > node.letter:
                path.append((node, "hi"))
                node = node.hi
                continue
            elif letter < node.letter:
                path.append((node, "lo"))
                node = node.lo
                continue
            else:
                path.append((node, "equal"))
                if index == len(word) - 1:
                    node.word_end = False
                    break
                node = node.equal
                index += 1

        while path and not node.lo and not node.hi and not node.equal and not node.word_end:  # type: ignore
            i, j = path.pop()
            if j == "lo":
                i.lo = None
            elif j == "hi":
                i.hi = None
            else:
                i.equal = None
            node = i
        return True

    def print_tst(self):
        """
        This function prints the current Ternary Search Tree, with the root and characters
        per word.
        """
        if not self._string_list:
            print("Tree is empty!")
            return
        print(f"terminates: {self._root.word_end}")
        print(
            f"       char: {self._root.letter}, terminates: {self._root.word_end}"
        )  # prints the root details
        nodes_to_print = []
        spaces = "  "
        if self._root.equal:
            nodes_to_print.append((self._root.equal, "_eq:", ""))
        if self._root.lo:
            nodes_to_print.append((self._root.lo, "_lo:", ""))
        if self._root.hi:
            nodes_to_print.append((self._root.hi, "_hi:", ""))

        while len(nodes_to_print):  # traverses the ternary search tree
            node_now, direction, current_spaces = nodes_to_print.pop(0)
            print(
                f"{direction}{current_spaces}      char: {node_now.letter}, terminates: {node_now.word_end}"
            )
            new_spaces = current_spaces + "  "
            if node_now.hi:
                nodes_to_print.append((node_now.hi, "_hi:", new_spaces))
            if node_now.lo:
                nodes_to_print.append((node_now.lo, "_lo:", new_spaces))
            if node_now.equal:
                nodes_to_print.append((node_now.equal, "_eq:", new_spaces))


def best_case(words):
    """
    This function builds a list of words for the best case with
    the words forming a balanced tree as much as possible.
    """
    words = sorted(words)
    best_words = []
    stack = [(0, len(words) - 1)]
    while len(stack) > 0:
        item = stack.pop()
        lo = item[0]
        hi = item[1]
        if hi >= lo:
            median = (lo + hi) // 2
            stack.append((lo, median - 1))
            stack.append((median + 1, hi))
            best_words.append(words[median])
        else:
            continue
    return best_words


def tests():
    tst = TernarySearchTree()
    with open("corncob_lowercase.txt", "r") as file:
        words = [line.strip() for line in file]

    unique_words = set(words)
    for word in unique_words:
        tst.insert(word)

    assert tst.len() == len(
        unique_words
    ), f"{tst.len()} in tree, expected {len(unique_words)}"

    for word in unique_words:
        assert tst.search(word), f"{word} not found"

    not_insert_words = ["hasselt", "diepenbeek", "arnhem"]
    for line in not_insert_words:
        word = line.strip()
        assert not tst.search(word), f"{word} should not be found"

    all_strings = tst.all_strings()
    assert len(all_strings) == len(
        unique_words
    ), f"{len(all_strings)} words, expected {len(unique_words)}"
    assert sorted(all_strings) == sorted(unique_words), "words do not match"


def main():
    tests()
    with open("corncob_lowercase.txt", "r") as file:
        words = [line.strip() for line in file]

    print(f"Loaded {len(words)} words")
    samples = [100, 500, 1000, 2000, 5000, 10000, 50000]
    nr_runs = 10

    average_words = sorted(words.copy())
    random.shuffle(average_words)

    word_cases = {
        "best case": best_case(sorted(words)),
        "average case": average_words,  # random shuffling of words
        "worst case": sorted(words),
    }  # original word (already ordered alphabetically)

    insert_times = {case: {} for case in word_cases}

    for case, words in word_cases.items():
        for N in samples:
            sample = words[:N]
            total_time = 0
            for _ in range(nr_runs):
                tree = TernarySearchTree()
                measurement_time = time.time_ns()
                for w in sample:
                    tree.insert(w)
                total_time += time.time_ns() - measurement_time
            insert_times[case][N] = (total_time / nr_runs) / 1_000_000

    print("Insert times (ms):")
    for case in insert_times:
        print(f"{case}: {insert_times[case]}")
    plt.figure()
    for case, times in insert_times.items():
        plt.plot(list(times.keys()), list(times.values()), label=case)
    plt.title("Insert Performance: Best Case vs Average Case vs Worst Case")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.savefig("insert_comparison.png")
    plt.close()

    search_times = {case: {} for case in word_cases}

    for case, words in word_cases.items():
        tree = TernarySearchTree()
        for w in words[: samples[-1]]:
            tree.insert(w)
        for N in samples:
            sample = words[:N]
            total_time = 0
            for _ in range(nr_runs):
                measurement_time = time.time_ns()
                for w in sample:
                    tree.search(w)
                total_time += time.time_ns() - measurement_time
            search_times[case][N] = (total_time / nr_runs) / 1_000_000

    print("\nSearch times (ms):")
    for case in search_times:
        print(f"{case}: {search_times[case]}")

    plt.figure()
    for case, times in search_times.items():
        plt.plot(list(times.keys()), list(times.values()), label=case)
    plt.title("Search Performance: Best Case vs Average Case vs Worst Case")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.savefig("search_comparison.png")
    plt.close()


if __name__ == "__main__":
    main()
  
