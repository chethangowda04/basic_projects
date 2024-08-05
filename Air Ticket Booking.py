print("Welcome to CGR bookings!!")
print(input("Enter User_id::"))
print(input("Enter Password::"))
print("""
Your Details:
Name     : Chethan Gowda R
Age      : 23
Location : Bengaluru
Bal_amt  :20000""")
choice = """
1) Domestic
2) International
3) Quit
"""
Total_amount = 20000
print("""
please select the location to travel.
1. Mumbai
2. Hyderebad
3. delhi
4. London
5. Canada
6. Australia
""")
Location = int(input("Select Location::"))
if 0 < Location <=6:

    Domestic_choices = {
        1: {"Airline": "Air India Express", "Price": 7000, "Seats": 10, "Departure": "10:00 AM", "Arrival": "12:00 PM"},
        2: {"Airline": "Quatar Airways", "Price": 5000, "Seats": 20, "Departure": "1:00 PM", "Arrival": "3:00 PM"},
        3: {"Airline": "Kingfisher", "Price": 3500, "Seats": 15, "Departure": "5:00 PM", "Arrival": "7:00 PM"},
        }


    International_choices = {
    1: {"Airline": "British Airlines", "Price": 15000, "Seats": 8, "Departure": "6:00 AM", "Arrival": "12:00 PM"},
    2: {"Airline": "Etihad Airways", "Price": 20000, "Seats": 12, "Departure": "8:00 AM", "Arrival": "2:00 PM"},
    3: {"Airline": "AirIndia", "Price": 25000, "Seats": 5, "Departure": "11:00 AM", "Arrival": "5:00 PM"},
    }

select = """
1) Book ticket
2) Cancel ticket
"""


def book_ticket(flight, Total_amount):
    if flight["Seats"] <= 0:
        print("please select the number of seats to travel.")
        return Total_amount
    if flight["Price"] > Total_amount:
        print("Insufficient funds")
        return Total_amount

    Total_amount -= flight["Price"]
    flight["Seats"] -= 1
    print(f"Your Ticket price is {flight['Price']}")
    print(f"Your Ticket has been booked with {flight['Airline']}")
    print(f"Departure Time: {flight['Departure']}")
    print(f"Arrival Time: {flight['Arrival']}")
    print(f"Remaining Balance: {Total_amount}")
    return Total_amount


def cancel_ticket(flight, Total_amount):
    Total_amount += flight["Price"]
    flight["Seats"] += 1
    print(f"Your Balance money is {Total_amount}")
    print(f"Your Ticket has been cancelled and your money has been refunded")
    return Total_amount


def quit_program():
    print("Thank you for choosing our site!!")
    exit()


while True:
    print(choice)
    user_choice = int(input("Enter the choice:"))

    flight = None

    if user_choice == 1:
        for key, details in Domestic_choices.items():
            print(
                f"{key}) {details['Airline']} - Rs:{details['Price']} - Seats available: {details['Seats']} - Dep: {details['Departure']} - Arr: {details['Arrival']}")
        user_choiceD = int(input("Enter the choice:"))
        flight = Domestic_choices.get(user_choiceD)

    elif user_choice == 2:
        for key, details in International_choices.items():
            print(
                f"{key}) {details['Airline']} - Rs:{details['Price']} - Seats available: {details['Seats']} - Dep: {details['Departure']} - Arr: {details['Arrival']}")
        user_choiceI = int(input("Enter the choice:"))
        flight = International_choices.get(user_choiceI)

    elif user_choice == 3:
        quit_program()

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue

    if flight is None:
        print("Invalid flight selection. Please try again.")
        continue

    print(select)
    user_select = int(input("Please select the option:"))

    if user_select == 1:
        Total_amount = book_ticket(flight, Total_amount)
    elif user_select == 2:
        Total_amount = cancel_ticket(flight, Total_amount)
    else:
        print("Invalid choice. Please select 1 or 2.")
