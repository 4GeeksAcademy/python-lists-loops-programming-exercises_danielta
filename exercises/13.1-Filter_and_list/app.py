all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def filter_names(name):
    return name[0].lower() == 'r'

resulting_names = list(filter(filter_names,all_names))

print(resulting_names)




