import random
import tracemalloc


def load_data():
    return [[random.random() for _ in range(784)] for _ in range(500)]


tracemalloc.start()
data = load_data()
snapshot = tracemalloc.take_snapshot()

print("Top 5 memory allocations:")
for stat in snapshot.statistics("lineno")[:5]:
    print(f"  {stat}")

print(f"Loaded {len(data)} rows of {len(data[0])} values")
