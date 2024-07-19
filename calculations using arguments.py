# argument with return function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
v1 = int(input("enter the number:"))
v2 = int(input("enter the number:"))
print("----------------------------")
print("select (1) for addition")
print("select (2) for subtraction")
print("select (3) for division")
print("select (4) for multiplication")
print("---------------------------------")
ch = int(input("enter your choice::"))
if ch == 1:
    print(f"{v1} + {v2} addition is::", add(v1,v2))
if ch == 2:
    print(f"{v1} - {v2} subtraction is::", sub(v1, v2))
if ch == 3:
    print(f"{v1} / {v2} division is::", div(v1, v2))
if ch == 4:
    print(f"{v1} * {v2} multiplication is::", mul(v1, v2))