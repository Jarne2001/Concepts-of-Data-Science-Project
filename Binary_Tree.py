import time
import random
import matplotlib.pyplot as plt

class BtreeNode:
    
    def __init__(self, string):
        self._string = string
        self._lt, self._gt = None, None

    def _insert(self, string):
        if string == self._string:
            return
        if string < self._string:
            if self._lt is None:
                self._lt = BtreeNode(string)
            else:
                self._lt._insert(string)
        elif string > self._string:
            if self._gt is None:
                self._gt = BtreeNode(string)
            else:
                self._gt._insert(string)
    
    def _search(self, string):
        if string == self._string:
            return True
        elif string < self._string:
            return self._lt is not None and self._lt._search(string)
        else:
            return self._gt is not None and self._gt._search(string)
    
    def _all_strings(self):
        strings = [self._string]
        if self._lt is not None:
            strings.extend(self._lt._all_strings())
        if self._gt is not None:
            strings.extend(self._gt._all_strings())
        return strings

    def __len__(self):
        length = 1
        if self._lt is not None:
            length += len(self._lt)
        if self._gt is not None:
            length += len(self._gt)
        return length

    def _to_string(self, indent=''):
        repr_str = indent + repr(self)
        if self._lt is not None:
            repr_str += '\n' + self._lt._to_string(indent + '  ')
        if self._gt is not None:
            repr_str += '\n' + self._gt._to_string(indent + '  ')
        return repr_str

    def __repr__(self):
        return self._string


class Btree:
    
    def __init__(self):
        self._root = None
        
    def insert(self, string):
        if self._root is None:
            self._root = BtreeNode(string)
        else:
            self._root._insert(string)

    def search(self, string):
        if self._root is None:
            return False
        else:
            return self._root._search(string)
        
    def all_strings(self):
        if self._root is None:
            return []
        else:
            return self._root._all_strings()
        
    def __len__(self):
        if self._root is None:
            return 0
        else:
            return len(self._root)
    
    def __repr__(self):
        if self._root is None:
            return 'empty tree'
        else:
            return self._root._to_string('')

def main():
    """
    This function allows to load in a word list into the main Binary Search Tree
    function for benchmarking.
    """
    # Load file
    with open('corncob_lowercase.txt', 'r') as file:
        words = [line.strip() for line in file]

    print(f"Loaded {len(words)} words")
    
    samples = [100, 500, 1000, 2000, 5000, 10000, 50000]
    
    # Test 1: Insert performance
    nr_runs = 10
    words = random.shuffle(words) # randomize word order to prevent skewed Btree
    insert_performance_times = {}

    for N in samples:
      sample = words[:N]
      measuring_time = 0
      for _ in range(nr_runs):
        btree = Btree()
        start_time = time.time_ns()
        for word in sample:
          btree.insert(word)
        end_time = time.time_ns()
        measuring_time += end_time - start_time
      insert_performance_times[N] = (measuring_time / nr_runs) * 1_000_000.0
    
    print(f"Insert times: {insert_performance_times}")     
    plt.figure()
    plt.plot(insert_performance_times.keys(), insert_performance_times.values())
    plt.title("Insert Performance")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.savefig('insert_performance.png')
    plt.close()
    
    # Test 2: Search performance
    search_performance_times = {}
    
    for N in samples:
      sample = words[:N]
      btree = Btree()
      for word in sample:
        btree.insert(word)
      measuring_time = 0
      for _ in range(nr_runs):
        start_time = time.time_ns()
        for word in sample:
          btree.search(word)
        end_time = time.time_ns()
        measuring_time += end_time - start_time
      search_performance_times[N] = (measuring_time / nr_runs) * 1_000_000.0
      
    print(f"Search times: {search_performance_times}")
    plt.figure()
    plt.plot(search_performance_times.keys(), search_performance_times.values())
    plt.title("Search Performance")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.savefig('search_performance.png')
    plt.close()
    print("Search done")
  
if __name__ == "__main__":
    main()
class BtreeNode:
    
    def __init__(self, string):
        self._string = string
        self._lt, self._gt = None, None

    def _insert(self, string):
        if string == self._string:
            return
        if string < self._string:
            if self._lt is None:
                self._lt = BtreeNode(string)
            else:
                self._lt._insert(string)
        elif string > self._string:
            if self._gt is None:
                self._gt = BtreeNode(string)
            else:
                self._gt._insert(string)
    
    def _search(self, string):
        if string == self._string:
            return True
        elif string < self._string:
            return self._lt is not None and self._lt._search(string)
        else:
            return self._gt is not None and self._gt._search(string)
    
    def _all_strings(self):
        strings = [self._string]
        if self._lt is not None:
            strings.extend(self._lt._all_strings())
        if self._gt is not None:
            strings.extend(self._gt._all_strings())
        return strings

    def __len__(self):
        length = 1
        if self._lt is not None:
            length += len(self._lt)
        if self._gt is not None:
            length += len(self._gt)
        return length

    def _to_string(self, indent=''):
        repr_str = indent + repr(self)
        if self._lt is not None:
            repr_str += '\n' + self._lt._to_string(indent + '  ')
        if self._gt is not None:
            repr_str += '\n' + self._gt._to_string(indent + '  ')
        return repr_str

    def __repr__(self):
        return self._string


class Btree:
    
    def __init__(self):
        self._root = None
        
    def insert(self, string):
        if self._root is None:
            self._root = BtreeNode(string)
        else:
            self._root._insert(string)

    def search(self, string):
        if self._root is None:
            return False
        else:
            return self._root._search(string)
        
    def all_strings(self):
        if self._root is None:
            return []
        else:
            return self._root._all_strings()
        
    def __len__(self):
        if self._root is None:
            return 0
        else:
            return len(self._root)
    
    def __repr__(self):
        if self._root is None:
            return 'empty tree'
        else:
            return self._root._to_string('')

def best_case(words):
    """
    This function builds a list of words for the best case with
    the words forming a balanced tree as much as possible.
    """
    words = sorted(words)
    best_words = []
    stack = [(0, len(words)-1)]
    while len(stack) >0:
        item = stack.pop(0)
        lo = item[0]
        hi = item[1]
        if hi >= lo:
          median = (lo + hi) // 2
          stack.append((lo, median-1))
          stack.append((median+1, hi))
          best_words.append(words[median])
        else:
          continue
    return best_words

def main():
    with open('corncob_lowercase.txt', 'r') as file:
        words = [line.strip() for line in file]

    print(f"Loaded {len(words)} words")
    samples = [100, 500, 1000, 2000, 5000, 10000, 50000]
    nr_runs = 10

    average_words = sorted(words.copy())
    random.shuffle(average_words)

    word_cases = {'best case': best_case(sorted(words)),
        'average case': average_words,  # random shuffling of words
        'worst case': sorted(words)} # original word (already ordered alphabetically)

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
    for case, time in insert_times.items():
        plt.plot(list(time.keys()), list(time.values()), label=case)
    plt.title("Insert Performance: Best Case vs Average Case vs Worst Case")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.savefig('insert_comparison_btree.png')
    plt.close()
    
    search_times = {case: {} for case in word_cases}

    for case, words in word_cases.items():
        tree = TernarySearchTree()
        for w in words[:samples[-1]]:
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
    for case, time in search_times.items():
        plt.plot(list(time.keys()), list(time.values()), label=case)
    plt.title("Search Performance: Best Case vs Average Case vs Worst Case")
    plt.xlabel("Tree size")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.savefig('search_comparison_btree.png')
    plt.close()

if __name__ == "__main__":
    main()
