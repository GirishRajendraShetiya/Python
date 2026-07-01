# Concurrency: Doing multiple tasks at a time (Texting someone while making tea). threading.Thread and asyncio.
# A single core having various threads, performing different tasks via different threads.

# It deals with threads.

# Parallelism: Running multiple tasks at the exact same time (2 friends making 2 different teas, not disturbing each other).
# If there is a video that needs to be processed, it'll be divided into small chunks and each chunk will be processed by a core of the CPU.
# But, if any of the core got occupied into some other important task, the further process will not be completed.
# multiprocessing.Process and concurrent.futures.ProcessPoolExecutor.

# It deals with processes.

# multithreading.py
import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
        
# create the threads
order_thread = threading.Thread(target=take_orders)  # The function name needs to be passed to the target argument of the Thread method.
brew_thread = threading.Thread(target=brew_chai)

# start the threads
order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")

# O/p:
# Taking order for #1
# Brewing chai for #1
# Taking order for #2
# Brewing chai for #2
# Taking order for #3
# Brewing chai for #3
# All orders taken and chai brewed

# multiprocessing.py
from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i + 1}", ))
        for i in range(3)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai served")

# O/p:
# Start of Chai Maker #1 chai brewing
# Start of Chai Maker #2 chai brewing
# Start of Chai Maker #3 chai brewing
# End of Chai Maker #1 chai brewing
# End of Chai Maker #2 chai brewing
# End of Chai Maker #3 chai brewing
# All chai served

