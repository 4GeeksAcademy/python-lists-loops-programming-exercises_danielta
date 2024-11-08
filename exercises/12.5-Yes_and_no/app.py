the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def new_names(array):
    for i in array:
        if i == 0:
            print('woko')
        else:
            print('wiki')

new_list = list(new_names(the_bools))

print(new_list)

# new_list = list(map(lambda x: 'wiki' if x==1 else 'woko', the_bools))

# print(new_list)