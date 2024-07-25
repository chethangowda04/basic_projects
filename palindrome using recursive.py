#palindrome using recusive function
def is_palindrome(l,r,s):
    if l>=r:
        return True
    if s[l] != s[r]:
        return False
    return is_palindrome (l+1, r-1, s)
my_string = input("enter your string::")
l = 0
r = len(my_string)-1

check = is_palindrome(l,r,my_string)
if check :
    print(f"{my_string} is palindrome")
else:
    print(f"{my_string} is not palindrome")