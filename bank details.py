#program to check whether the account details given is valid that given at the run time, if it is valid give the account holder details
id = 911
acc_num = "sbi 613"

Id = int(input("enter Id:"))
Acc_num = input("enter Acc_num:")

if id==Id and acc_num==Acc_num:
    print("""
    Bank Name           : State Bank Of india
    account holder name : Chethan Gowda R
    type of account     : Savings
    balance amount      : 911613.89Rs
          """)
else:
    print(f"the entered Id '{Id}' or Acc_num '{Acc_num}' is wrong")