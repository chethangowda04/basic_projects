#loop with list items
fruits =  ["mango", "apple", "grapes","peach"]
for f in fruits:
    for i in f:
        print(i, end ="*")
    print()

fruits =  ["mango", "apple", "grapes","peach"]
for f in fruits:
    for i in f:
        print(f, end ="*")
    print()


colour = ["red", "green", "yellow"]
items = ["apple", "veggies", "dress"]
for x in colour:
    for y in items:
        print(x,y)
        #print()
    print()


#append 2 lists
l1 = [10, 20, 30]
l2 = [40, 50, 60]
result = []
for i in l1:
    for j in l2:
        result.append(i+j)
    print(result)


#multiplying two lists
list1 = [2,4,6,8]
list2 = [2,4,6,8]
for i in list1 :
    for j in list2:
        if i == j:
            continue
        print(i, "*", j, "=", i*j)
