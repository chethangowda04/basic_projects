#nesting of loop
#rhombus pattern
for r in range(1,6):
    for c in range(1,r+1):
        print(c, end=" ")
    print()

for r in range(6,1,-1):
    for c in range(1,r+1):
        print(c, end=" ")
    print()
for r in range(6,1,-1):
    for c in range(1,r-1,-1):
        print(c, end=" ")
    print()

for r in range(1,6):
    for c in range(1,r+1):
        print("*", end="  ")
    print()
for r in range(6,1,-1):
    for c in range(1,r):
        print("*", end="  ")
    print()



for x in range(-6,1):
    for y in range(-x):
        print(y, end =" ")
    print(" ")
