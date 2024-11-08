my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds():
    sum = 0
    for i in range(0,len(my_list)):
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    return(sum)
print(sum_odds())
