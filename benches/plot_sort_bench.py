import time
import random
import sys
import matplotlib.pyplot as plt

sys.path.append(".")

from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort
from sorting.merge_sort import merge_sort

def benchmark(sort_fn, data):
    start = time.perf_counter()
    sort_fn(data.copy())
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    data = [random.randint(0, 10000) for _ in range(3000)]

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
    }

    times = []
    names = []

    for name, fn in algorithms.items():
        t = benchmark(fn, data)
        times.append(t)
        names.append(name)

    plt.figure()
    plt.bar(names, times)
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithms Performance Comparison")
    plt.tight_layout()
    plt.savefig("plots/sorting_benchmark.png")
    plt.show()
