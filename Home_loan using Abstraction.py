###Home loan using Abstraction###
from abc import ABC
class RBI(ABC):
    loan=int(input("enter the loan amount::"))
    def home_loan(self):
        pass
    def education_loan(self):
        pass
    def vehicle_loan(self):
        pass
class SBI(RBI):
    def home_loan(self):
            return self.loan*0.3
    def education_loan(self):
            return self.loan * 0.2
    def vehicle_loan(self):
            return self.loan * 0.1
class HDFC(RBI):
    def home_loan(self):
            return self.loan*0.35
    def education_loan(self):
            return self.loan * 0.2
    def vehicle_loan(self):
            return self.loan * 0.15
class Barath(RBI):
    def home_loan(self):
            return self.loan*0.3
    def education_loan(self):
            return self.loan * 0.25
    def vehicle_loan(self):
            return self.loan * 0.12
sb=SBI()
hd=HDFC()
bh=Barath()
choice=input("""Select the choice of the bank from which you want to take the loan 
1)SBI 
2)HDFC 
3)KARNATAKA """)
if choice=="SBI":
    loan_type=input("""We provide 
1 vehicle loan
2 home loan
3 education loan
Please enter the type of loan you need::""")
    if loan_type=="vehicle loan":
        print("The interest of vehicle loan in sbi",sb.vehicle_loan())
    elif loan_type=="home loan":
        print("The interest of home loan in sbi",sb.home_loan())
    elif loan_type == "education loan":
        print("The interest of education loan in sbi",sb.education_loan())
elif choice=="HDFC":
    loan_type = input("enter the type of loan you need::")
    if loan_type == "vehicle loan":
        print("The interest of interest of vehicle loan in Hdfc",hd.vehicle_loan())
    elif loan_type == "home loan":
        print("The interest of home loan in Hdfc",hd.home_loan())
    elif loan_type == "education loan":
        print("The interest of education loan in Hdfc",hd.education_loan())
elif choice=="BARATH":
    loan_type = input("enter the type of loan you need::")
    if loan_type == "vehicle loan":
        print("The interest of vehicle loan in KARNATAKA",bh.vehicle_loan())
    elif loan_type == "home loan":
        print("The interest of home loan in KARNATAKA",bh.home_loan())
    elif loan_type == "education loan":
        print("The interest of education loan in KARNATAKA",bh.education_loan())