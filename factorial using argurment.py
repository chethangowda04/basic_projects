#no arguement no return function
def factorial_number():
    factorial = 1
    num = int(input("enter a number to get its facorial::"))
    for i in range (1, num+1):
        factorial = factorial * i
    print("the factorial is ::", factorial)
factorial_number()
