import os

def process_data(data):
    total = 0
    for item in data:
        for i in range(1000):
            total += int(item)
    return total

def duplicate_code_example(data):
    total = 0
    for item in data:
        for i in range(1000):
            total += int(item)
    return total

def insecure_function():
    user_input = input("Enter command: ")
    eval(user_input)  # SECURITY RISK

def overly_long_function(a, b):
    if a > b:
        print("A is greater")
    elif a < b:
        print("B is greater")
    else:
        print("Equal")
    for i in range(10):
        print(i)
    for j in range(5):
        print(j * j)
    if a + b > 100:
        print("Sum too large!")
    if a * b > 1000:
        print("Product too large!")
    return a + b

def unused_function():
    pass
