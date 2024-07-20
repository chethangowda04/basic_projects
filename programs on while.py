##while loop
i = 5
while (i>0):
    j = 5
    while(j<i):
        print("*", end=" ")
        j = j-1
    i = i-1
    print()





#to print the sum of even numbers
a = 1
while a<=50:
    sum = 0
    for i in range(1,a):
        if i%2 == 0:
            sum += i
    a = a + 1
print("the sum of even number is::", sum)



#fruits

fruits = ["apple", "mango", "grapes", "kiwi"]
for f in fruits:
    count = 0
    while count<6:
        print(f, end=" ")
        count += 1
    print()
