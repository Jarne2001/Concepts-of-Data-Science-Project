import matplotlib.pyplot as plt
import time

# first load the data set in HPC, here is an example for test only
words = ["combine", "combinations", "combination", "combined", "combines","ducks", "ducked", "duck","futile", "futility", "future",
         "fontain", "font","far", "a", "the", "their", "therefor", "there","bomb"]
sizes = [100, 500, 1_000, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000] # example sizes like the jupyter, I dont know how value of the large data file
samples = []

for size in sizes:
    samples.append(words[:size])

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
    times[len(sample)] /= nr_runs*1_000_000.0
times

plt.plot(times.keys(), times.values())
plt.show()

# Test 2: Search performance
nr_runs = 10
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
    times[len(sample)] /= nr_runs*1_000_000.0
times
plt.plot(times.keys(), times.values())
plt.show()

# Test 3: Search from sample
nr_runs = 10
times = {}
for sample in samples:
    tst = TernarySearchTree()
    for word in sample:
        tst.insert(word)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        search_sample = sample[:20]
        start_time = time.time_ns()
        for word in search_sample:
            tst.search(word)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
times
plt.plot(times.keys(), times.values())
plt.show()
