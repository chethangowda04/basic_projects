#print only even numbers in the given list and find their sum
lst = [23,48,24,67,87,4,23,78]
sum = 0
for i in lst :
    if i%2==0:
        print(i)
        sum += i
print("the sum  is::", sum)