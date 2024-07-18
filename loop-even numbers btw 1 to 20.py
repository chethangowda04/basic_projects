#print odd and even numbers bw 1 to 20 and find their sum
sum=0
print("even number")
for x in range(1,21):
    if x%2==0:
        print(x)
        sum+=x
print("the sun of even is::", sum)
print("-------------------------------------------")
print("odd number")
for x in range(1,21):
    if x%2!=0:
        sum+=x
        print(x)
print("the sum of odd num is", sum)