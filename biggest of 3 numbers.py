#program to check the biggest of 3 numbers
a = int(input("enter a value:"))
b = int(input("enter b value:"))
c = int(input("enter c value:"))
if a>b and a>c:
    print(f"{a} is bigger than {b} & {c}")
elif b>c and b>a:
    print(f"{b} is bigger than {a} & {c}")
elif c>a and c>b:
    print(f"{c} is bigger than {a} & {b}")



