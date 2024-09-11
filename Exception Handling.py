###Value Error, Zero Division Error###
# print ("Handlling exception using try.....except.....else.....finally")
# try:
#     numerator = 50
#     denom = int(input("enter the denominator::"))
#     quotient = (numerator/denom)
#     print(quotient, "Division performed successfully")
# except ZeroDivisionError:
#     print("denominator as zero is not allowed")
# except ValueError:
#     print("only integers should be entered")
# else:
#     print("the result of division operator is:", quotient)
# finally:
#     print("over and out")




###key Error###
# prices = {'pen':10, 'pencil':5, 'notebook':25}
# item = input("get the price of ::")
# try:
#     print(f"the price of {item} is {prices[item]}")
# except KeyError:
#     print(f"the price of {item} is not known")
# else:
#     print("there is no error in statement")


###Value Error in finding factorial of number###
# print("trying to display the factorial")
# try:
#     fact = 1
#     num = int(input("enter any number::"))
#     for x in range (1, num+1):
#         fact *= x
#         print(f"the factorial of {x} is::", fact)
# except ValueError:
#     print("only integers should be entered")
# else:
#     print("finally got the answer")
# finally:
#     print("the code its answer")



###raising error###
# def square_data(numbers):
#     if not isinstance(numbers,(list,tuple or set)):
#         raise TypeError(f"list or tuple excepted,got '{type(numbers)._name_}")
#     return [numbers**2 for numbers in numbers]
#
# print(square_data([1,2,3,4,5]))
# print(square_data({1,2,3,4,5}))
