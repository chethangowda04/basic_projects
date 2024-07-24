
Total_amount = 200000
name=input("Enter the name:")
password=input("enter the password:")
print("welcome to karnataka bank !")


def withdraw(money,Total_amount):
    Total_amount -= money
    print(f"Your Bank Balance is {Total_amount}")
def deposit(money,Total_amount):
   Total_amount+=money
   print(f"Your Bank Balance is {Total_amount}")
def logout():
     print("Thank you")
     print("visit again")


choice = [withdraw, deposit, logout]
for i in choice:
    choices = """
    1)withdraw
    2)deposit
    3)logout
    """
    print(choices)
    user_choice=int(input("enter the choice:"))
    if user_choice == 1:
        money = int(input("enter the money to withdraw"))
        withdraw(money, Total_amount)

    if user_choice == 2:
        money = int(input("enter the money to deposit"))
        deposit(money, Total_amount)

    if user_choice == 3:
        print("Thank you!!")
        break









