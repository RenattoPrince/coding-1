import multiprocessing as mp
import os
import numpy as np
import time

def worker(duration, result_queue):
    count = 0
    num = 1

    end_time = time.time() + duration

    while time.time() < end_time:
        num = (num * 1234567) % 987654321
        count += 1

    result_queue.put(count)

def benchmark(duration=10):
    cpu_count = os.cpu_count()

    print("=" * 40)
    print("MULTI-CORE CPU BENCHMARK")
    print("=" * 40)
    print(f"CPU Cores Available: {cpu_count}")
    print(f"Benchmark Duration: {duration} seconds")
    print()

    result_queue = mp.Queue()

    processes = [
        mp.Process(
            target=worker,
            args=(duration, result_queue)
        )
        for _ in range(cpu_count)
    ]

    start = time.time()

    for p in processes:
        p.start()

    total_operations = 0

    for _ in processes:
        total_operations += result_queue.get()

    for p in processes:
        p.join()

    elapsed = time.time() - start

    print("Results:")
    print(f"Total Operations: {total_operations:,}")
    print(f"Operations/Second: {total_operations / elapsed:,.0f}")
    print(f"Benchmark Score: {(total_operations / elapsed) / 1_000_000:.2f} MOPS")

if __name__ == "__main__":
    mp.freeze_support()  # Windows compatibility
    benchmark()
    

