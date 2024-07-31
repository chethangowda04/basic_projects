#list comprehensions

squares = [x**2 for x in range (11)]
print(squares)

city1 = ['paris', 'london', 'berlin', 'tokyo', 'sydney']
city2 = []
city2 = [x for x in city1]
print("city2:", city2)


numbers = [1,2,3,4,5,6,7,8,9,10]
even_no = []
even_no = [i for i in numbers if i%2 == 0]
print(even_no)



list1 = ['q', 'a', 't', 'd', 'o', 'f', 'e']
list2 = ['a','e', 'i', 'o', 'u']
result =  [i for i in list1 for j in list2 if i ==j]
print(result)

words = ['filtering', 'words', 'based', 'on', 'length']
five_ltrs = [i for i in words if len(i) == 5]
print(five_ltrs)


my_fruit = ["apple", "banana", "orange", "mango"]
my_fruit2 = [i[0] for i in my_fruit]
print(my_fruit2)

mixed_list = ["apple", "banana", 12,15, 7, 2, 3, "orange", "mango"]
mixed_list2 = [i**2 if type(i) == int else i[0] for i in mixed_list]
print(mixed_list2)

#using list comprehension with functions
def power(x):
    return x**2
p_num = []
for x in range (1,10):
    p_num.append(power(x))
print(p_num)


# nested list comprehension

nstd = [[1,2],[3,4],[5,6]]
elements = [i for pair in nstd for i in pair]
print(elements)

list1 = [1,2,3]
list2 = ["a", "b", "c"]
pairs = [(x,y) for x in list1 for y in list2]
print(pairs)



#1. generate a set of common elements from two sets
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
common = [i for i in list1 for j in list2 if i ==j]
print(common)


# #2. WAP to generate pair of distinct elements and their character
list1 = ['abc', 'def', 'ghi']
list2 = ['jkl', 'mno', 'pqr']
pairs = [(i,j) for i in list1 for j in list2]
print(pairs)
print(ord())



#3. create pairs of distinct elements and their absolute difference from two
list1 = [3,6,9]
list2 = [5,10,15]
dis = [(i,j) for i in list1 for j in list2]
difference = [abs(i-j) for i in list1 for j in list2]
print(dis)
print("difference::", difference)


#4. write a list comprehension to display numbers and their binary representation from 1 to 10
binary = [bin(n) for n in range (1,11)]
print(binary)




# #5.write a list comprehension to display numbers and their factorial from 1 to 10

import math
fac = [math.factorial(x) for x in range(1,11)]
print(fac)