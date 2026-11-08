# async - Could be used in place of multithreading & multiprocessing.

# async def - It declares a co-routine, a special function that can be paused.
# await - Could be used only when the function is async, pauses the execution until the result is ready
# Event loop - The engine that runs and schedule the co-routines

# Widely used in the API.

import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)  # await is a NON-BLOCKING way to simulate waiting 
    print("Chai is ready")

asyncio.run(brew_chai())

# O/p:
# Brewing chai...
# Chai is ready

import asyncio

async def brew_chai(name):
    print(f"Brewing {name} chai...")
    await asyncio.sleep(2)
    print(f"{name} is ready")

async def main():
    # Below is the co-routine
    await asyncio.gather(
        brew_chai("Masala"),
        brew_chai("Ginger"),
        brew_chai("Lemon")
    )

asyncio.run(main())

# It waited for COMBINED 2 seconds, NOT EVERY TIME 2 seconds, as await performs the non-blocking operation.
# O/p:
# Brewing Masala chai...
# Brewing Ginger chai...
# Brewing Lemon chai...
# Masala is ready
# Ginger is ready
# Lemon is ready

# If instead of await, time is used, it'll take 2 seconds everytime.

import asyncio
import time

async def brew_chai(name):
    print(f"Brewing {name} chai...")
    # await asyncio.sleep(2)
    time.sleep(2)
    print(f"{name} is ready")

async def main():
    # Below is the co-routine
    await asyncio.gather(
        brew_chai("Masala"),
        brew_chai("Ginger"),
        brew_chai("Lemon")
    )

asyncio.run(main())

# O/p:
# Brewing Masala chai...
# Masala is ready
# Brewing Ginger chai...
# Ginger is ready
# Brewing Lemon chai...
# Lemon is ready

# Blocking - time.sleep(2)
# Non-blocking - await asyncio.sleep(2)

# Spread operator (*) - To un-pack the stuffs.
# tasks = [t1, t2, t3]

# with open(*tasks) It's basically means un-packing the tasks list

# Combination of asyncio and multi-threading
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# A normal function, NOT a async co-routine
def validate_stock(item):
    print(f"Validating the stock for {item}")
    time.sleep(3)
    return f"{item}: 42"

# async co-routine
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        # The run_in_executor separates the above validate_stock method from blocking the main thread
        # to running into a separate thread
        # Basically, it has converted a normal function to work as an async one
        result = await loop.run_in_executor(pool, validate_stock, "Masala Chai")
        print(result)

asyncio.run(main())

# O/p:
# Validating the stock for Masala Chai
# Masala Chai: 42

# Combination of asyncio and multi-processing
import asyncio
from concurrent.futures import ProcessPoolExecutor

def data_encrypt(data):
    return f"{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, data_encrypt, "Masala Chai")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

# O/p: iahC alasaM

# asyncio and multi-threading
import asyncio
import threading
import time

def bg_worker():
    while True:
        time.sleep(1)
        print("Logging system details")

async def fetch_orders():
    await asyncio.sleep(4)
    print("Order fetched")

threading.Thread(target = bg_worker, daemon = True).start()

asyncio.run(fetch_orders())

# O/p:
# Logging system details
# Logging system details
# Logging system details
# Logging system details
# Order fetched

# daemon, non-daemon threads

# Daemon - They are the background threads which automatically shuts down when the main program exit. Used for non-critical background tasks, like logging & monitoring.

import threading
import time

def validate_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)
        
t = threading.Thread(target = validate_tea_temp, daemon = True)
t.start()

print("Main program done.")

# O/p:
# Monitoring tea temperature...
# Main program done.

# Non-daemon

import threading
import time

def validate_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)
        
t = threading.Thread(target = validate_tea_temp)
t.start()

print("Main program done.")

# O/p:
# Main program done.Monitoring tea temperature...

# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...

# Deadlock
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task_1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")

def task_2():
    with lock_b:
        print("Task 2 acquired lock b")
        with lock_a:
            print("Task 2 acquired lock a")

t1 = threading.Thread(target = task_1)
t2 = threading.Thread(target = task_2)

t1.start()
t2.start()

# O/p:
# Task 1 acquired lock a
# Task 2 acquired lock b
