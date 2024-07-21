#LIST

my_list = ['p', 'r', 'o', 'b', 'P', 'e', 'm']
subject = ['maths','science','social',['kannada','english','hindi'],'sanskrit']
print(subject[3][2])
print(my_list[0])

#negative indexing
my_list = ['p','r','o','b','e']
print(my_list[-1])
print(my_list[-5])

# #slicing
my_list = ['p','r','o','b','e']
print(len(my_list))
print(my_list[2:5])


# #negative slicing
my_list = ['p','r','o','b','e','g','c','h']
print(my_list[5:])
print(my_list[:])
print(my_list[:5])
print(my_list[:-6])

#change list elements
even = [2,4,6,8]
print(even)
even[0] = 1 #change the 1st item
print(even)
even[1:3] = [3,5,7] #change 1st to 3rd items
print(even)

#adding by using append and extending list in python
even = [1,3,5]
even.append([7,8,9])
print(even)
even.extend([10,11,12])
print(even)

#deleting list items

my_list = ['p', 'r', 'o', 'b', 'e', 'g', 'c', 'h']
del my_list[2]
print(my_list)

del(my_list[1:5]) #deleting multiple items
print(my_list)

del my_list[:]
print(my_list)

#using remove,pop,clear
my_list = ['p', 'r', 'o', 'b', 'e', 'g', 'c', 'h']
my_list.remove('p')
print(my_list)
print(my_list.pop(4))
print(my_list)

my_list.clear()
print(my_list)
res = my_list.pop(4)
print(res)
print(my_list)

#sort python list
##ascending order
mylist = [21,5,8,52,21,87,52]
mylist.sort() #ascending order
print(mylist)
mylist.sort(reverse=True) #descending order
print(mylist)
