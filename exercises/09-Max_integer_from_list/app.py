my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(array):
    biggest = array[0]
    for i in range(0,len(array)):
        if array[i] > biggest:
            biggest = array[i]
        else:
            None
    return(biggest)

print(max_integer(my_list))