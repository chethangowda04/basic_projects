#args
def add(*num):
    sum = 0
    for n in num:
        sum +=n
    print("sum is:", sum)
add(2,6)
add(2,4,6,8)
add(1,2,3,4,5,6,7,8,9)

#kwargs
def person(**kwargs):
    for key, value in kwargs.items():
        print("{} ---- {}". format(key, value))
person (name = "chethan", gen = "male", age = 23, city = "magadi", mobile = "9110462859")

def func(a,b, *args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)
func(1,3,10,20,name = 'Tom', salary=60000 )


def intro(**data):
    print("\n datatype of argument:", type(data))
    for key, value in data.items():
        print("{} is {}" .format(key, value))
intro(firstname="sita", lastname="sharma", age=23, phone=9080706050)
intro(firstname="radha", lastname="krishna", age=33, phone=9080706051, country="India", email="radhakrishna@gmail.com",)