#finding reverse using revursive function

def reverse_list (my_list, l, r):
    if l>=r:
        return my_list
    #swap
    tem = my_list[l]
    my_list[l] = my_list[r]
    my_list[r] = tem
    return reverse_list(my_list, l+1, r-1)
my_l = [3,1,5,4,7]
l = 0
r = len(my_l)-1
print('my_list:', my_l)
print("reverse of list:", reverse_list(my_l,l,r))