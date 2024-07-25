#recursive function
##to find factorial using recursive function
def factorial (x):
    if x == 1:
        return 1
    else:
        return (x*(factorial(x-1)))
num = int(input("enter the number::"))
print("factorial of given numer", num,"is",factorial(num))