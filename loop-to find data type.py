#program that print item and thats data type in the given list
datalist = [1234, 11.23, True, "Be Practical", (0, -1), [5,12], {"class":'V', "section":'A'}]
for i in datalist:
    print(f"the element is {i}",type(i))
