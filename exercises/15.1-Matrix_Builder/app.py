# Your code here
# def matrix_builder(x): 
#     for i in range(0,x):


def matrix_builder(size, default_value=0):
    result = [default_value] * size
    return [result] * size

print(matrix_builder(3, 1))