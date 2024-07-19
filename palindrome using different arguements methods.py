#palindrome with arguement with return function
def is_palindrome(num):
    num = str(num)
    rev = num[::-1]
    if num == rev:
        return True
    else:
        return False
n1 = 797
result = is_palindrome(n1)
if result:
    print(f"{n1} is a palindrome.")
else:
    print(f"{n1} is not a palindrome.")


#plaindrome with arguement without return function
def is_palindrome(num):
    num = str(num)
    rev = num[::-1]
    if num == rev:
        print(f"the given number {n} is palindrome")
    else:
        print(f"the given number {n}is not a palindrome")
# n = 242
n = int(input("enter any number::"))
res = is_palindrome(n)

# palindrome without arguement with return function
def find_palindrome():
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        def is_palindrome(n):
            return str(n) == str(n)[::-1]
        original_num = num
        while True:
            if is_palindrome(num):
                print(f"The palindrome of {original_num} is: {num}")
                return num
            else:
                num += 1
    else:
        print("Invalid input. Please enter a valid number.")
find_palindrome()



#palindrome with no arguement and no return function
num = int(input("enter any number:"))
rev = 0
temp = num
while num!=0:  #while num>0
    digit = num%10
    rev = rev*10+digit
    num//= 10
print("the reverse of the number is::", rev)
if rev == temp:
    print("is palindrome")
else:
    print("is not palindrome")
