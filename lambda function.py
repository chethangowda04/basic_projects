##lambda fucntion
x = lambda a,b:(a*b)
print(x(5,6))


name_list = ["grass hopper", "ada lovelace", "emmy noether", "marie curie"]
sorted_by_surname = sorted(name_list, key = lambda x: x.split()[1])
print(sorted_by_surname)



def add (a,b):
    return(lambda x:a+b)
f = add(3,4)(0)
print(f)

#
res = lambda x:(x%2 and "odd" or "even")
print(res(14))

str = lambda string: string in "welcome to the world of lambda functions in python"
print(str("python"))


strngs = ['a', 'b', 'c', 'd', 'e']
numbers = [1,2,3,4,5]
res = list(map(lambda x,y:(x,y),strngs,numbers))
print(res)


wrds = ["hgkgh", "mom", "radar", "mnvb"]
palindrome = list(filter(lambda word:word == word[::-1],wrds))
print(palindrome)

#double of each number
num = [1,2,3,4,5]
dou = list(map(lambda x:x*2,num))
print(dou)

from functools import reduce
numbers = [1,2,3,4,5]
total = reduce(lambda x ,y: x+y,numbers)
print(total)