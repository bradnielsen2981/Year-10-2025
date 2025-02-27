import math

def add(a, b):
    total = a+b
    return total

def subtract(a, b):
    total = a-b
    return total

def pythag(a=4, b=3):
    c = math.sqrt(a**2 + b**2)
    return

side = pythag(10,13)
print(side)


def powers(c,d):
    cat = c**d
    dog = d**c
    return cat, dog

cd, dc = powers(3,2)
print(cd)
print(dc)




print(pythag())

rA = input("Enter the first number: ")
rA = float(rA)
rB = input("Enter the second number: ")
rB = float(rB)

result = add(rA, rB)
print("The result is: ", result)
result = subtract(rA, rB)
print("The result is: ", result)
result = pythag(rA, rB)
print("The result is: ", result)
# nameoffunction() -> calling the function