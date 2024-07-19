#no arguement with return function
my_list = [23,44,66,74,23]
def add_list():
    sum = 0
    for list_item in my_list:
        sum += list_item
    return sum
result = add_list()
print("the sum is::", result)