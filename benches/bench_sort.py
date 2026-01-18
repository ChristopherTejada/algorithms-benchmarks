import time
import random
import sys

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

    results = {
        "Bubble Sort": benchmark(bubble_sort, data),
        "Quick Sort": benchmark(quick_sort, data),
        "Merge Sort": benchmark(merge_sort, data),
    }

    for name, t in results.items():
        print(f"{name}: {t:.6f}s")
