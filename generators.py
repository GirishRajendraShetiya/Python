# Memory efficient
# No immediate results
# yield and next keywords are used

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Elaichi Chai"
    yield "Cup 3: Hot Chai"
    
stall = serve_chai()

for cup in stall:
    print(cup)

# O/p:
# Cup 1: Masala Chai
# Cup 2: Elaichi Chai
# Cup 3: Hot Chai

def return_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def generate_chai_list():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = generate_chai_list()
print(chai)  # <generator object generate_chai_list at 0x7f0f75e38a90>

# Using the next function to generate the next values
def generate_chai_list():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = generate_chai_list()
print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
print(next(chai))  # StopIteration Error

# Types:
# 1. Infinite
def infinite_chai():
    count = 1
    while True:
        yield f"Refill: {count}"
        count += 1
        
refill = infinite_chai()

for _ in range(5):
    print(next(refill))

# O/p:
# Refill: 1
# Refill: 2
# Refill: 3
# Refill: 4
# Refill: 5

# 2. Send
def chai_customer():
    print("Welcome to the Car Store")
    order = yield # It stops the execution of the code and waits for the input to the yield field
    while True:
        print(f"Preparing: {order}")
        order = yield
        
stall = chai_customer()
next(stall)  # It initiates the generator

# stall.send("Mercedes")
# stall.send("Lambhorghini")

# O/p: Welcome to the Car Store

def chai_customer():
    print("Welcome to the Car Store")
    order = yield # It stops the execution of the code and waits for the input to the yield field
    while True:
        print(f"Preparing: {order}")
        order = yield
        
stall = chai_customer()
next(stall)  # It initiates the generator

stall.send("Mercedes")  # It sends the data to the yield field which gets to the order field and then to the while loop,
# post which the order field waits again for the input.
stall.send("Lambhorghini")

# O/p:
# Welcome to the Car Store
# Preparing: Mercedes
# Preparing: Lambhorghini

