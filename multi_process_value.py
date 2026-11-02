from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)  # Using value, the data between processes could be shared
    processes = [Process(target = increment, args = (counter, )) for _ in range(4)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    
    print(f"Final counter value: {counter.value}")

# O/p: Final counter value: 400000
