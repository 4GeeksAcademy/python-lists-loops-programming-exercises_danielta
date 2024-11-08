list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

def sort_odd_even(array):
    even = []
    sorted_list = []
    for i in range(0, len(array)):
        if array[i] % 2 != 0:
            sorted_list.append(array[i])
        else: 
            even.append(array[i])
    for i in range(0,len(even)):
        sorted_list.append(even[i])
    return(sorted_list)


print(sort_odd_even(list_of_numbers))

