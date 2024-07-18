#print multiplication table format of any given number
tb = int(input("enter the number to be multiplied:"))
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(f"{tb}*{i}=",tb*i)


#factorial
num = int(input("enter any number:"))
fact = 1
for x in range(1,num+1):
    fact = fact * x
print(f"the factorial of number {num} is:", fact)
