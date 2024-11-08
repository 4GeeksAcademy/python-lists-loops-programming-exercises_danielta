


def lyrics_generator(array):
    string = ""
    for i in range(0,len(array)):
        if array[i] == 1: 
            string += "Drop the bass "
            if i >= 2 and array[i-1] == 1 and array[i-2] == 1:
                string += "!!!Break the bass!!! "
        elif array[i] == 0:
            string += "Boom "
    return string
        
            


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
