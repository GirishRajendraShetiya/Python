# It provides a mutex (mutual exclusive lock) which avoids 2 threads to update a data at the same time.

# concurrency - multithreading
import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing process.")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing process.")

thread1 = threading.Thread(target = brew_chai, name = "Barista1")
thread2 = threading.Thread(target = brew_chai, name = "Barista2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")

# O/p:
# Barista1 started brewing process.
# Barista2 started brewing process.
# Barista2 finished brewing process.
# Barista1 finished brewing process.
# Total time taken: 20.24 seconds

# parallelism - multiprocessing
from multiprocessing import Process
import time

def crunch_number():
    print("Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Ended the count process...")
    
start = time.time()

p1 = Process(target = crunch_number)
p2 = Process(target = crunch_number)

p1.start()
p2.start()
p1.join()
p2.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")  # It'll throw a RunTime Error if not ran via the __name__ == "__main__"

# O/p: RunTime Error

from multiprocessing import Process
import time

def crunch_number():
    print("Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Ended the count process...")
    
if __name__ == "__main__":
    start = time.time()

    p1 = Process(target = crunch_number)
    p2 = Process(target = crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken: {end - start:.2f} seconds")

# O/p:
# Started the count process...
# Started the count process...
# Ended the count process...
# Ended the count process...
# Total time taken: 16.50 seconds

import threading
import time

def boil_milk():
    print("Boiling milk ...")
    time.sleep(2)
    print("Done boiling milk ...")
    
def toast_bun():
    print("Toasting bun ...")
    time.sleep(3)
    print("Done toasting bun ...")
    
t1 = threading.Thread(target = boil_milk)
t2 = threading.Thread(target = toast_bun)

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Breakfast done in {end - start:.2f} seconds")

# O/p:
# Boiling milk ...
# Toasting bun ...
# Done boiling milk ...
# Done toasting bun ...
# Breakfast done in 3.00 seconds

# Passing arguments to the threading function
import threading
import time

def prepare_chai(type_, wait_time):
    print(f"Preparing {type_} chai")
    time.sleep(wait_time)
    print(f"Your {type_} chai is ready")
    
t1 = threading.Thread(target = prepare_chai, args = ("Masala", 2))
t2 = threading.Thread(target = prepare_chai, args = ("Ginger", 3))

t1.start()
t2.start()
t1.join()
t2.join()

# O/p:
# Preparing Masala chai
# Preparing Ginger chai
# Your Masala chai is ready
# Your Ginger chai is ready

# Download images via threading
import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
    ]
    
start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target = download, args = (url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
end = time.time()

print(f"Total time: {end - start:.2f} seconds")

# O/p:
# Starting download from https://httpbin.org/image/jpeg
# Starting download from https://httpbin.org/image/png
# Starting download from https://httpbin.org/image/svg
# Finished downloading from https://httpbin.org/image/svg, size: 8984 bytes
# Finished downloading from https://httpbin.org/image/png, size: 8090 bytes
# Finished downloading from https://httpbin.org/image/jpeg, size: 35588 bytes
# Total time: 32.82 seconds

# Thread lock
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target = increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")

# O/p: Final counter: 1000000
