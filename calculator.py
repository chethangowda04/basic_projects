#program to demonstrate a calculator
A = int(input("enter the a value:"))
B = int(input("enter the b value:"))
print("""
select the operator:
1:'+'
2:'-'
3:'*'
4:'/'
""")
operator = int(input())
if operator==1:
    print(f"the sum of {A} and {B} is:",A+B)
elif operator==2:
    print(f"the difference of {A} and {B} is:",A-B)
elif operator==3:
    print(f"the multiplication of {A} and {B} is:",A*B)
elif operator==4:
    print(f"the division of {A} and {B} is:",A/B)
else:
    print("select valid operator ")