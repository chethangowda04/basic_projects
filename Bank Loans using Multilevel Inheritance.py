###Bank Loans using Multilevel Inheritance
class Bank_Loan:
    def bank_info(self):
        print("We give all types of loans......")

class Home_Loan(Bank_Loan):

    def Hloan_amt(self):
        print("Home loan amount details...")
        H_amt=int(input("Enter the amount::"))
        if H_amt<4000000 or H_amt>2000000:
            rate_interest= H_amt * 0.50
            print(rate_interest)
        elif H_amt<2000000 or H_amt>1000000:
            rate_interest= H_amt *0.25
            print(rate_interest)


class Vehicle_Loan(Home_Loan):

    def Vloan_amt(self):
        print("Vehicle loan amount details...")
        V_amt = int(input("Enter the amount::"))
        if V_amt < 2000000 or V_amt > 1000000:
            rate_interest = V_amt * 0.50
            print(rate_interest)
        elif V_amt < 1000000 or V_amt > 500000:
            rate_interest = V_amt * 0.25
            print(rate_interest)
class Education_loan(Vehicle_Loan):

    def Eloan_amt(self):
        print("Home loan amount details...")
        E_amt = int(input("Enter the amount::"))
        if E_amt < 2000000 or E_amt > 1000000:
            rate_interest = E_amt * 0.50
            print(rate_interest)
        elif E_amt < 500000 or E_amt > 1000000:
            rate_interest = E_amt * 0.25
            print(rate_interest)

HL=Education_loan()
HL.bank_info()
HL.Hloan_amt()
HL.Vloan_amt()
HL.Eloan_amt()