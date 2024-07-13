# program to manage Rental Shop
print("Welcome to CGR RENTALS")
print("enter your name:")
Name = input("")
print("enter your age:")
age = int(input())
if age<18:
    print("the person age is not eligible to get vehicle to ride")
else:
    print("enter DL_No:")
DL_No = input("")
print("select the type of vehicle:")
print("""
1: Two Wheeler
2: Four Wheeler
""")
vehicle_type = int(input())
if vehicle_type==1:
    print("""
    select bike model
    1: Dio
    2: Splender
    3: Royal Enfield
    4: Dominar 400
    """)
    bike_model = int(input())
    if bike_model==1:
        print("Dio")
        print("rent per hour is 120Rs")
        print("enter hour")
        hour = float(input())
        print("vehicle cost")
        cost = (hour*120)
        print(cost)
        total_cost = cost+0.12*cost
        print(total_cost)
    if bike_model==2:
        print("Splender")
        print("rent per hour is 120Rs")
        print("enter hour")
        hour = int(input())
        print("vehicle cost")
        cost = (hour * 120)
        print(cost)
        total_cost = cost + 0.12 * cost
        print(total_cost)
    if bike_model==3:
        print("Royal Enfield")
        print("rent per hour is 180Rs")
        print("enter hour")
        hour = int(input())
        print("vehicle cost")
        cost = (hour * 180)
        print(cost)
        total_cost = cost + 0.12 * cost
        print(total_cost)
    if bike_model==4:
        print("Dominar 400")
        print("rent per hour is 200Rs")
        print("enter hour")
        hour = int(input())
        print("vehicle cost")
        cost = (hour * 200)
        print(cost)
        total_cost = cost + 0.12 * cost
        print(total_cost)