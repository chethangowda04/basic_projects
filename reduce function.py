#reduce function
from functools import reduce
numbers = [3,4,6,12,34,21]
print(numbers)
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum,numbers)
print(result)

from functools import reduce
numbers = [1,2,3,4,5]
total = reduce(lambda x ,y: x+y,numbers)
print(total)