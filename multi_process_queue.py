import threading
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print("Done")
    
start_time = time.time()

threads = [threading.Thread(target = cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

end_time = time.time()

print(f"Time taken: {end_time - start_time:.2f} seconds ")
