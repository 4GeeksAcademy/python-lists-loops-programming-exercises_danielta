celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius):
    return((celsius*9/5)+32)
#     result = []
#     for i in celsius:
#         result.append((i * 9/5)+32)
#     return(result)

# print(celsius_to_fahrenheit(celsius_values))

# Dont change the code below:
result = list(map(celsius_to_fahrenheit, celsius_values))

print(result)
