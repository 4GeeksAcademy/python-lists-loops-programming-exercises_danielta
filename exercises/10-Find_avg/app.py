my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

# Your code here
def find_avg(array):
    sum=0
    for i in range(0,len(array)):
        sum += array[i]
    average = sum/len(array)
    return(average)

print(find_avg(my_list))