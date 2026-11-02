from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**8):  # In comparison to the threads, Process could process quite a large amount of data.
        total += i
    print("Done")

if __name__ == "__main__":
    start_time = time.time()
    
    processes = [Process(target = cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds ")
