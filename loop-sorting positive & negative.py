 #program to seperate positive and negative num in given list
pos = []
neg = []
x = [23,4,-6,23,-9,21,3,-45,-8]
for i in x:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)

x = [23,4,-6,23,-9,21,3,-45,-8]
print(f"positive number in {x} is:")
for i in x:
    if i>0:
        print(i)

print(f"the negative number in {x} is:")
for i in x:
    if i<0:
        print(i)

