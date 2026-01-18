import time
import random
import sys

sys.path.append(".")

from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort

def benchmark(sort_fn, data):
    start = time.perf_counter()
    sort_fn(data.copy())
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    data = [random.randint(0, 10000) for _ in range(2000)]

    bubble_time = benchmark(bubble_sort, data)
    quick_time = benchmark(quick_sort, data)

    print(f"Bubble Sort: {bubble_time:.6f}s")
    print(f"Quick Sort:  {quick_time:.6f}s")
