#to check the entered character is vowel or constant
A = input("enter the alphabet:")
if A=="a" or A=="e" or A=="i" or A=="o" or A=="u":
    print(f"the given alphabet '{A}' is vowel")
else:
    print(f"the given alphabet '{A}' is constant")