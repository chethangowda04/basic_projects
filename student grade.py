#to accept marks for 5 subjects, calculate total and average, display the result, based on the average find the result of student
#if avg>95 distinction
#btw 65 and 95 then FC
#btw 40 and 65 then TC
#else fail
eng = int(input("enter english marks out of 100:"))
kan = int(input("enter kannada marks out of 100:"))
hin = int(input("enter hindi marks out of 100  :"))
mat = int(input("enter mat marks out of 100    :"))
sci = int(input("enter sci marks out of 100    :"))

total = eng+kan+hin+mat+sci
print(f"total marks is:{total}")

average = total/5
print(f"{total}/5")
print(f"average marks is:{average}")

if average>=95:
    print("distinction")
elif 65<=average<95:
    print("first class")
elif 45<=average<65:
    print("second class")
elif 35<=average<45:
    print("third class")
else:
    print("fail")