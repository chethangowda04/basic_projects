
# ##set comprehension
words = ['apple', 'banana', 'cherry', 'pmpkn']
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_words = {i for i in words if any(j in vowels for j in i)}
print(vowel_words)

my_list = [1,2,3,4,5,6,7,8,9,10]
new_set = {i*3 for i in my_list}
print("the existing list is::", my_list)
print("the newly created list is::", new_set)

myset = {1,2,3,4,5,6,7,8,9,10}
newset = {i**2 for i in myset}
print("the existing set is::", myset)
print("the newly created set is::", newset)

fear = ("the only thing we have to fear is fear itself")
res = len({i for i in fear.split() if 't' not in i})
print(res)


#set of reversed strings from another set
words = {"apple", "banana", "cherry"}
reversed_words = {word[::-1] for word in words}
print(words)
print(reversed_words)

#to get only digits from string
string ="1234hello5678"
digits = {i for i in string if i.isdigit()}
print(digits)

numbers ={1,2,3,4,5}
squared_numbers = {x**2 for x in numbers}
print(squared_numbers)

def is_prime(n):
    if n<=1:
        return False
    for i in range (2, int(n**0.5) +1):
        if n%i==0:
            return False
    return True
prime_numbers = {x for x in range (1,51) if is_prime(x)}
print(prime_numbers)


#set of even  number squared and odd number cubed from 1 to 10
result = {x**2 if x%2==0 else x**3 for x in range (1,11)}
print(result)

#set of unique number from a list
numbers = [1,2,3,4,2,5,3,1,6]
unique_numbers = {x for x in numbers}
print(unique_numbers)


#set of squares from a set of numbers
import math
num = [1,4,9,16,25]
num_sqrt = {math.sqrt(x) for x in num}
print(num)
print(num_sqrt)