par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
for i in par:
    i = i.lower()
    if par[i] == ' ':
        None
    elif i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print(counts)
