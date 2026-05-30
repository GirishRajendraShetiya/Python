# Global keyword:

x = 10

def func():
    global x
    x = 15
    
print(x)  # 10
func()
print(x)  # 15

a = 1

def modify_a(value):
    global a
    a = value
    
print(a)  # 1
modify_a(7)
print(a)  # 7

# nonlocal keyword: Scope to an enclosing function. Used only in nested functions.
# Also, where the keyword is used, that respective function needs to be called.

def outer():
    tea_pack = "Ginger"
    
    def inner():
        nonlocal tea_pack
        tea_pack = "Plain"
    
    inner()
    
    return tea_pack
    
print(outer())  # Plain

def outer():
    tea_pack = "Ginger"
    
    def inner():
        nonlocal tea_pack
        tea_pack = "Plain"
    
    # inner()
    
    return tea_pack
    
print(outer())  # Ginger

def outer():
    tea_pack = "Ginger"
    
    def inner():
        tea_pack = "Plain"
    
    inner()
    
    def inner_1():
        nonlocal tea_pack
        tea_pack = "Masala"
    
    # inner_1()
    
    return tea_pack
    
print(outer())  # Ginger

def outer():
    tea_pack = "Ginger"
    
    def inner():
        tea_pack = "Plain"
    
    inner()
    
    def inner_1():
        nonlocal tea_pack
        tea_pack = "Masala"
    
    inner_1()
    
    return tea_pack
    
print(outer())  # Masala
