##dictionary comprehensions
squares = {x: x**2 for x in range(1,11)}
print(squares)

even_squared = {x:x**2  for x in range(0,21) if x%2==0}
print(even_squared)

#dictionary of words and their length from a sentence
words = "python is awesome"
word_length = {word:len(word) for word in words.split()}
print(word_length)


#dictionary of number and their cubes
numbers = [1,2,3,4,5]
cubes = {x:x**3 for x in numbers}
print(cubes)


dictionary of numbers and their prime values
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n%i == 0:
            return False
    return True
numbers = [1,2,3,4,5,6,7,8,9,10]
prime_status = {x: is_prime(x) for x in numbers}
print(prime_status)

#dictionary of words and the count of vowels from a list of strings
words = ['apple', 'banana', 'cherry']
vowel_count ={word:sum(1 for char in word if char.lower() in 'aeiou') for word in words}
print(vowel_count)


#dictionary of words and their reversed forms
words = ['apple', 'banana', 'cherry']
reversed_words = {word:word[::-1] for word in words}
print(reversed_words)

#create a dictionary of numbers and their parity even or odd
numbers = [1,2,3,4,5,6,7,8,9,10]
pair_num = {i:'even' if i%2==0 else 'odd' for i in numbers}
print(pair_num)


create a dictionary of number and their factorials
import math
numbers = [1,2,3,4,5]
fac = {x:math.factorial(x) for x in numbers}
print(fac)