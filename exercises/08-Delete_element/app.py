people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    new_list=[]
    for i in range(0,len(people)):
        if people[i].lower() != person_name:
            new_list.append(people[i])
        else:
            None
    return(new_list)
    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
