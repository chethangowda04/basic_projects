print("welcome to CGR AirBookings")
print("1:Domestic     2:Internatinal")
print("Please select the flight type")

# def flight_varient(flight_type):
flight_type = int(input( ))
if flight_type == 1:
    print("""
    1:Quatar Airways
    2:IndiGo
    """)
    print("Please select Flight")
    flight = int(input())
    if flight == 1:
        print("""you selectd Quatar Airways
        enter the location from you have to travel """)

if flight_type == 2:
    print("""
    1:Air India
    2:British Airways
    """)
    print("Please select Flight")













# # Function to display available flights
# def display_flights():
#     print("Available Flights:")
#     print("1. Flight A100 - New York to Los Angeles")
#     print("2. Flight B200 - Chicago to San Francisco")
#     print("3. Flight C300 - Miami to Seattle")
#
#
# # Function to book a flight
# def book_flight(flight_number):
#     if flight_number == 1:
#         print("Flight A100 from New York to Los Angeles booked successfully!")
#     elif flight_number == 2:
#         print("Flight B200 from Chicago to San Francisco booked successfully!")
#     elif flight_number == 3:
#         print("Flight C300 from Miami to Seattle booked successfully!")
#     else:
#         print("Invalid flight number. Please select a valid flight.")
#
#
# # Main function to run the program
# def main():
#     display_flights()
#     while True:
#         try:
#             choice = int(input("Enter the flight number you want to book (1-3): "))
#             if choice in [1, 2, 3]:
#                 book_flight(choice)
#                 break
#             else:
#                 print("Invalid input. Please enter a number between 1 and 3.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#
#
# if __name__ == "__main__":
#     main()
